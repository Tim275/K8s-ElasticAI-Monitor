# Testing app

```sh
python3 app.py

docker build -t jonathanbaraldi/flask-log-generator:latest .

docker run -d -p 5000:5000 jonathanbaraldi/flask-log-generator:latest

docker logs -f 

docker login

jonathanbaraldi

docker push jonathanbaraldi/flask-log-generator:latest

kubectl apply -f deployment.yaml


curl http://18.221.23.124:5000/variable_not_found
curl http://localhost:5000/repeated_log
curl http://localhost:5000/division_by_zero
curl http://localhost:5000/log_large_data
curl http://localhost:5000/frequent_logs
curl http://localhost:5000/generate_mixed_logs


curl http://flask.k8s.devopsforlife.io/generate_mixed_logs

curl http://flask.k8s.devopsforlife.io/variable_not_found
curl http://flask.k8s.devopsforlife.io/repeated_log
curl http://flask.k8s.devopsforlife.io/division_by_zero
curl http://flask.k8s.devopsforlife.io/log_large_data
curl http://flask.k8s.devopsforlife.io/frequent_logs
curl http://flask.k8s.devopsforlife.io/generate_mixed_logs


```

```sh

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

# Run the loop for 5 minutes (300 seconds)
while [ $(($(date +%s) - $start_time)) -lt 300 ]; do
    for url in "${urls[@]}"; do
        echo "Hitting URL: $url"
        curl -s $url > /dev/null  # Add -s to make curl silent and redirect output to /dev/null
    done
    sleep 2  # Optional sleep to slow down the iterations
done

echo "Completed 5 minutes of hitting the URLs."


```


