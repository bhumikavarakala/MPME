import json
import http.client
from urllib.parse import urlencode

PROMETHEUS_URL = "localhost:9090"

def monitor_environment(cpu_query='sum(rate(container_cpu_usage_seconds_total[1m])) by (namespace)'):
    """Queries Prometheus to monitor environment CPU usage."""
    conn = http.client.HTTPConnection(PROMETHEUS_URL)

    # Build query parameters
    params = urlencode({'query': cpu_query})

    # Make the GET request
    conn.request("GET", f"/api/v1/query?{params}")

    # Get the response
    response = conn.getresponse()

    if response.status == 200:
        # Read and parse JSON response
        data = json.loads(response.read().decode())
        results = data.get('data', {}).get('result', [])
        
        for result in results:
            namespace = result['metric'].get('namespace', 'unknown')
            cpu_usage = result['value'][1]
            print(f"Namespace '{namespace}' CPU usage: {cpu_usage}")
    else:
        print(f"Error querying Prometheus: {response.status}")

    # Close the connection
    conn.close()


