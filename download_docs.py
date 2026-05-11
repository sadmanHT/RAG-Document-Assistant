import os
import requests
from markdownify import markdownify

# Define the Kubernetes documentation URLs
URLS = {
    "pods": "https://kubernetes.io/docs/concepts/workloads/pods/",
    "deployments": "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/",
    "services": "https://kubernetes.io/docs/concepts/services-networking/service/",
    "configmaps": "https://kubernetes.io/docs/concepts/configuration/configmap/",
    "namespaces": "https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/",
    "replicasets": "https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/",
    "statefulsets": "https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/",
    "daemonsets": "https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/",
    "ingress": "https://kubernetes.io/docs/concepts/services-networking/ingress/",
    "persistent_volumes": "https://kubernetes.io/docs/concepts/storage/persistent-volumes/",
    "resource_quotas": "https://kubernetes.io/docs/concepts/policy/resource-quotas/",
    "labels_and_selectors": "https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/",
    "components": "https://kubernetes.io/docs/concepts/overview/components/"
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
