import sys
from pathlib import Path

# Ensure the parent directory is in sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.generation import ask

def main():
    print("Kubernetes Docs Assistant — type your question or type exit to quit")
    while True:
        try:
            query = input("\n> ").strip()
            if query.lower() == 'exit':
                print("Goodbye!")
                break
            if not query:
                continue
            
            # Get the generated answer & citations
            result = ask(query)
            
            # Print the formatted output
            print("\nAnswer:")
            print(result.get('answer', 'No answer generated.'))
            print("\nSources:")
            for source in result.get('sources', []):
                print(f"- {source}")
                
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nOops! An error occurred: {e}")
            print("You can try your question again.")

if __name__ == '__main__':
    main()
