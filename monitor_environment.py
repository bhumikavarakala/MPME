import requests

PROMETHEUS_URL = "http://localhost:9090"

def monitor_environment(cpu_query='sum(rate(container_cpu_usage_seconds_total[1m])) by (namespace)'):
    """Queries Prometheus to monitor environment CPU usage."""
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': cpu_query})
    if response.status_code == 200:
        results = response.json().get('data', {}).get('result', [])
        for result in results:
            namespace = result['metric'].get('namespace', 'unknown')
            cpu_usage = result['value'][1]
            print(f"Namespace '{namespace}' CPU usage: {cpu_usage}")
    else:
        print(f"Error querying Prometheus: {response.status_code}")
