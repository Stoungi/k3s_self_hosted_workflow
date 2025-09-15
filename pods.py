import subprocess
import json
from collections import defaultdict

def get_pods_by_namespace():
    """
    Retrieves all Kubernetes pods and groups them by namespace.

    This script uses the 'kubectl' command-line tool to get a list of all
    pods in a JSON format. It then organizes the pods into a dictionary
    where each key is a namespace and the value is a list of pods in that 
    namespace.

    Returns:
        A dictionary with namespaces as keys and lists of pods as values.
        Returns an empty dictionary if an error occurs.
    """
    try:
        # Use subprocess to run the 'kubectl get pods' command with JSON output
        command = ["kubectl", "get", "pods", "--all-namespaces", "-o", "json"]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Parse the JSON output
        pod_data = json.loads(result.stdout)
        
        # The pod information is under the 'items' key
        pods = pod_data.get("items", [])
        
        # Use defaultdict to automatically create a list for each new namespace
        pods_by_namespace = defaultdict(list)
        for pod in pods:
            namespace = pod['metadata']['namespace']
            pods_by_namespace[namespace].append(pod)
            
        return dict(pods_by_namespace)
    
    except FileNotFoundError:
        print("Error: 'kubectl' command not found. Please ensure it is installed and in your system's PATH.")
        return {}
    except subprocess.CalledProcessError as e:
        print(f"Error executing kubectl command: {e}")
        print(f"Stderr: {e.stderr}")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON output from kubectl.")
        return {}

if __name__ == "__main__":
    namespaces = get_pods_by_namespace()
    if namespaces:
        print("Found the following Kubernetes pods, grouped by namespace:")
        for namespace, pods in namespaces.items():
            print(f"\n--- **Namespace**: {namespace} ---")
            for pod in pods:
                # Extract key information for each pod
                name = pod['metadata']['name']
                status = pod['status']['phase']
                
                # Print a formatted string for each pod
                print(f"  - **Name**: {name}, **Status**: {status}")
    else:
        print("No pods found or an error occurred.")