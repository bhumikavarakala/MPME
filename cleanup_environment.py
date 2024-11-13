import subprocess

def delete_namespace(env_name="staging"):
    """Deletes a Kubernetes namespace."""
    try:
        subprocess.run(["kubectl", "delete", "namespace", env_name], check=True)
        print(f"Namespace '{env_name}' deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Error deleting namespace '{env_name}'.")

def cleanup_helm_release(env_name="staging"):
    """Cleans up Helm release by deleting the associated environment namespace."""
    try:
        subprocess.run(["helm", "uninstall", env_name, "--namespace", env_name], check=True)
        delete_namespace(env_name)
        print(f"Cleanup for environment '{env_name}' completed.")
    except subprocess.CalledProcessError:
        print(f"Failed to clean up Helm release for environment '{env_name}'.")
