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
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from src.generation import ask

def robust_generate_and_eval():
    load_dotenv()
    
    eval_dir = Path(__file__).parent
    golden_file = eval_dir / "golden_dataset.json"
    results_file = eval_dir / "results.json"
    
    with open(golden_file, "r", encoding="utf-8") as f:
        golden_dataset = json.load(f)
        
    print(f"Loaded {len(golden_dataset)} evaluation questions. Running sequentially with retry/delays...")
    
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("GROQ API Key missing.")
        sys.exit(1)
        
    ragas_llm = ChatGroq(model="llama-3.1-8b-instant", api_key=api_key)
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
                 # Note: ask internally utilizes Groq API in generation.py
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
                
                # Suppress the exception raising inside evaluate so rate limits don't crash the script run immediately
                res = evaluate(dataset=ds, metrics=metrics_list, llm=ragas_llm, embeddings=ragas_embeddings, raise_exceptions=False)
                print(f"DEBUG {i}: {res}")

                for m in ["faithfulness", "answer_relevancy", "context_precision"]:
                    val = res.get(m, 0.0)
                    import math
                    if math.isnan(val):
                        print(f"DEBUG {i}: Metric {m} is NaN! Setting to 0.0 to avoid poisoning sum.")
                        val = 0.0
                    totals[m] += val
                success_count += 1
                break
            except Exception as e:
                print(f"  [!] Evaluate Error (rate limits/network): {e}\n  Retrying in 60 seconds...")
                time.sleep(60)

        # Print running averages
        print("\n--- Current Running Averages ---")
        for m in totals:
            avg = totals[m] / success_count if success_count > 0 else 0.0
            print(f"{m:<20}: {float(avg):.4f}")
        print("--------------------------------\n")

        # 4. Delay to prevent rate limits on Groq
        if i < len(golden_dataset) - 1:
            print("  Sleeping 60 seconds to respect Groq rate limits...")
            time.sleep(60)

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