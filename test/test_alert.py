import requests
import json
import time

# Simulated Elasticsearch watcher payload
test_data = [
    {
        "doc_count": 100,
        "key": "ERROR: Database connection failed\n"
    },
    {
        "doc_count": 50,
        "key": "WARNING: High CPU usage detected\n"
    }
]

def test_alert():
    try:
        # Send test data to Flask endpoint
        response = requests.post(
            "http://localhost:5000/alert",
            headers={"Content-Type": "application/json"},
            json=test_data,
            timeout=30
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_alert()