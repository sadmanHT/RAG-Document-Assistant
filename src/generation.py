import os
import re
import yaml
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

from src.retrieval import retrieve_and_rerank

# Load environment variables
load_dotenv()

# Load prompts
config_path = Path("config/prompts.yaml")
with open(config_path, "r", encoding="utf-8") as f:
    prompts = yaml.safe_load(f)

system_prompt = prompts.get("system_prompt", "You are a helpful assistant.")
rag_prompt_template = prompts.get("rag_prompt_template", "Context: {context}\n\nQuestion: {query}")

# Initialize Gemini model
api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", google_api_key=api_key)

def generate_answer(query, context_chunks):
    formatted_contexts = []
    unique_sources = set()
    
    for i, chunk in enumerate(context_chunks):
        source = chunk["metadata"].get('source', 'Unknown')
        unique_sources.add(source)
        # Format as requested
        formatted = f"[Source: {source} | Chunk {i}]\n{chunk['text']}"
        formatted_contexts.append(formatted)
        
    context_str = "\n\n".join(formatted_contexts)
    
    # Fill template
    prompt_text = rag_prompt_template.format(context=context_str, question=query)
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=prompt_text)
    ]
    
    response = llm.invoke(messages)
    
    return {
        'answer': response.content,
        'sources': list(unique_sources)
    }

def enforce_citation(answer, context_chunks):
    # Stopwords to ignore
    stopwords = {"the", "is", "a", "an", "of", "and", "to", "in", "for", "with", "on", "as", "it", "this", "that", "are", "be"}
    
    # Simple sentence extraction using regex (split by . ? !)
    sentences = [s.strip() for s in re.split(r'[.?!]', answer) if s.strip()]
    if not sentences:
        return True # Edge case: no sentences
        
    combined_context = " ".join([chunk["text"].lower() for chunk in context_chunks])
    
    grounded_count = 0
    for sentence in sentences:
        words = [w.lower() for w in re.findall(r'\b\w+\b', sentence) if w.lower() not in stopwords]
        
        # Check if ANY of the significant words appear in context
        has_grounding = False
        for word in words:
            if word in combined_context:
                has_grounding = True
                break
                
        if has_grounding:
            grounded_count += 1
            
    ratio = grounded_count / len(sentences)
    return ratio >= 0.5

def ask(query):
    # Get chunks
    ranked_chunks = retrieve_and_rerank(query, top_k_final=5)
    
    # Generate Answer
    result = generate_answer(query, ranked_chunks)
    
    # Enforce Citation
    is_grounded = enforce_citation(result['answer'], ranked_chunks)
    
    if not is_grounded:
        result['answer'] = 'Insufficient evidence found in the documentation to answer this question.'
        
    return result

if __name__ == '__main__':
    query = 'how do I create a deployment in kubernetes'
    print(f"Query: {query}\n")
    response = ask(query)
    print("Answer:\n", response['answer'])
    print("\nSources:\n", response['sources'])
