import os
import requests
from markdownify import markdownify

# Define the Kubernetes documentation URLs
URLS = {
    "pods": "https://kubernetes.io/docs/concepts/workloads/pods/",
    "deployments": "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/",
    "services": "https://kubernetes.io/docs/concepts/services-networking/service/",
    "configmaps": "https://kubernetes.io/docs/concepts/configuration/configmap/",
    "namespaces": "https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/"
}

# Ensure the output directory exists
OUTPUT_DIR = os.path.join("data", "raw")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_and_convert(name, url):
    print(f"Downloading {name} docs from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        
        # Convert HTML to Markdown
        md_content = markdownify(response.text, heading_style="ATX")
        
        # Save to file
        file_path = os.path.join(OUTPUT_DIR, f"{name}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        
        print(f"Saved: {file_path}")
    except Exception as e:
        print(f"Failed to download or process {name}: {e}")

def main():
    for name, url in URLS.items():
        download_and_convert(name, url)
        
if __name__ == "__main__":
    main()
