#!/bin/bash

# Define the URLs
urls=(
    "http://flask.k8s.devopsforlife.io/variable_not_found"
    "http://flask.k8s.devopsforlife.io/repeated_log"
    "http://flask.k8s.devopsforlife.io/division_by_zero"
    "http://flask.k8s.devopsforlife.io/log_large_data"
    "http://flask.k8s.devopsforlife.io/frequent_logs"
    "http://flask.k8s.devopsforlife.io/generate_mixed_logs"
)

# Get the current timestamp
start_time=$(date +%s)

# Run the loop for 10 minutes (600 seconds)
while [ $(($(date +%s) - $start_time)) -lt 600 ]; do
    for url in "${urls[@]}"; do
        echo "Hitting URL: $url"
        curl -s -w "\nHTTP status: %{http_code}\n" $url  # Waits for server response, showing the HTTP status
    done
done

echo "Completed 5 minutes of hitting the URLs."
