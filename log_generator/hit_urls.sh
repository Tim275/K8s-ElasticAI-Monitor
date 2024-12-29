#!/bin/bash

# Define the URLs

urls=(
    "http://flask.timourproject.com/variable_not_found"
    "http://flask.timourproject.com/repeated_log"
    "http://flask.timourproject.com/division_by_zero"
    "http://flask.timourproject.com/log_large_data"
    "http://flask.timourproject.com/frequent_logs"
    "http://flask.timourproject.com/generate_mixed_logs"
)


start_time=$(date +%s)


while [ $(($(date +%s) - $start_time)) -lt 600 ]; do
    for url in "${urls[@]}"; do
        echo "Hitting URL: $url"
        curl -s -w "\nHTTP status: %{http_code}\n" $url  
    done
done

echo "Completed 5 minutes of hitting the URLs."
