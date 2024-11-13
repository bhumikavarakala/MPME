Description: Documentation for your repository. Save this as README.md.

markdown
Multi-Project Multi-Environment (MPME) Automation

This repository contains Python scripts to automate environment setup, deployment, monitoring, and cleanup in Kubernetes using Helm and Prometheus.

Repository Contents

create_environment.py: Creates a Kubernetes namespace for a specific environment (`staging`).
- deploy_application.py: Deploys an application to Kubernetes using Helm.
- monitor_environment.py: Monitors CPU usage for namespaces in Kubernetes by querying Prometheus.
- cleanup_environment.py: Cleans up Helm releases and deletes the environment namespace.

