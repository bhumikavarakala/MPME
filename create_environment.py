import subprocess

def create_namespace(env_name="staging"):
    """Creates a Kubernetes namespace for a given environment."""
    try:
        subprocess.run(["kubectl", "create", "namespace", env_name], check=True)
        print(f"Namespace '{env_name}' created successfully.")
    except subprocess.CalledProcessError:
        print(f"Namespace '{env_name}' already exists or an error occurred.")
