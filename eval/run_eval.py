import sys
import json
import os
import time
from datetime import datetime
from pathlib import Path
import warnings

# Suppress numpy warnings from Ragas when answers contain no statements
warnings.filterwarnings('ignore', message='Mean of empty slice', category=RuntimeWarning)

# Add project root to sys.path so we can import src
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
from datasets import Dataset

from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from src.generation import ask

# Monkey-patch to fix the ragas temperature kwargs bug with the new GenAI SDK
class PatchedGemini(ChatGoogleGenerativeAI):
    def generate_prompt(self, *args, **kwargs):
        kwargs.pop("temperature", None)
        time.sleep(20) # Hard delay to prevent Free Tier 5 RPM limit
        return super().generate_prompt(*args, **kwargs)
    def generate(self, *args, **kwargs):
        kwargs.pop("temperature", None)
        time.sleep(20) # Hard delay to prevent Free Tier 5 RPM limit
        return super().generate(*args, **kwargs)

def robust_generate_and_eval():
    load_dotenv()
    
    eval_dir = Path(__file__).parent
    golden_file = eval_dir / "golden_dataset.json"
    results_file = eval_dir / "results.json"
    
    with open(golden_file, "r", encoding="utf-8") as f:
        golden_dataset = json.load(f)
        
    print(f"Loaded {len(golden_dataset)} evaluation questions. Running sequentially with heavy retry/delays...")
    
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("API Key missing.")
        sys.exit(1)
        
    ragas_llm = PatchedGemini(model="gemini-3.1-flash-lite-preview", google_api_key=api_key)
    ragas_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    metrics_list = [faithfulness, answer_relevancy, context_precision]
    
    totals = {"faithfulness": 0.0, "answer_relevancy": 0.0, "context_precision": 0.0}
    success_count = 0
    
    for i, entry in enumerate(golden_dataset):
        question = entry["question"]
        ideal_answer = entry["ideal_answer"]
        print(f"\n[{i+1}/{len(golden_dataset)}] Question: {question}")
        
        # 1. Robust Generation (retries indefinitely)
        while True:
            try:
                 # Note: ask internally utilizes Gemini 2.5 flash in generation.py
                result = ask(question)
                break
            except Exception as e:
                print(f"  [!] Ask Error (rate limits/network): {e}\n  Retrying in 60 seconds...")
                time.sleep(60)
                
        # 2. Format single item into RAGAS Dataset
        ds = Dataset.from_dict({
            "question": [question],
            "answer": [result.get("answer", "")],
            "contexts": [result.get("sources", [])],
            "ground_truth": [ideal_answer]
        })
        
        # 3. Robust Evaluation (retries indefinitely) 
        while True:
            try:
                print("  evaluating metrics...")
                # Note: internal evaluate makes multiple prompt calls behind the scenes
                res = evaluate(dataset=ds, metrics=metrics_list, llm=ragas_llm, embeddings=ragas_embeddings)
                
                for m in ["faithfulness", "answer_relevancy", "context_precision"]:
                    val = res.get(m, 0.0)
                    totals[m] += val
                success_count += 1
                break
            except Exception as e:
                print(f"  [!] Evaluate Error (rate limits/network): {e}\n  Retrying in 60 seconds...")
                time.sleep(60)

        # 4. Delay to prevent 429 Resource Exhausted on Gemini Free Tier
        # RAGAS internally triggers ~3 requests per metric. 
        # A 30s delay between items easily guarantees we never hit the 15/RPM limit
        if i < len(golden_dataset) - 1:
            print("  Sleeping 30 seconds to respect free-tier quotas...")
            time.sleep(30)
        
    # Final Output Report
    print("\n" + "="*30)
    print("RAGAS Evaluation Results")
    print("="*30)
    
    final_scores = {}
    import math
    for m in totals:
        avg = totals[m] / success_count if success_count > 0 else 0.0
        if math.isnan(avg):
            avg = 0.0
        final_scores[m] = float(avg)
        print(f"{m:<20}: {float(avg):.4f}")
        
    is_passing = bool(final_scores.get("faithfulness", 0.0) >= 0.85)
    print("Status: " + ("PASS" if is_passing else "FAIL"))
    print(f"Results saved to eval/results.json")
    print("="*30 + "\n")
    
    output_report = {
        "timestamp": datetime.now().isoformat(),
        "metrics": final_scores,
        "pass": is_passing,
        "total_evaluated": success_count
    }
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(output_report, f, indent=4)
        
    if not is_passing:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    robust_generate_and_eval()