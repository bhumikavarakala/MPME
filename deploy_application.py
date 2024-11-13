import subprocess

def deploy_with_helm(env_name="staging", chart_path="./helm/myapp", values_file="./helm/values-staging.yaml"):
    """Deploys an application using Helm with specific environment values."""
    try:
        subprocess.run([
            "helm", "upgrade", "--install", env_name, chart_path,
            "-f", values_file,
            "--namespace", env_name
        ], check=True)
        print(f"Deployment for environment '{env_name}' initiated successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to deploy Helm chart in environment '{env_name}'.")
