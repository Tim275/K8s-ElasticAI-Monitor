

# Ollama - GenAI

## 14. Infrastructure Deployment - Machine

t3.xlarge  - Dont load any model
p3.2xlarge -  3 USD per hour
r5.2xlarge - 0,5 per hour

=>c5.xlarge  -  $0.17 4 8 GiB 

inf2.xlarge - On-Demand Linux pricing 0.7582 USD per Hour

Choosed machined.

=> c5.2xlarge  -  $0.34 8/16 GiB 









## 15. Deployment ollama and llama3


```sh
cd /Users/jonathanbaraldi/Dropbox/hotmart_aiops_logs/genai

ssh -i pic.pem ubuntu@18.191.107.234

sudo su

curl https://releases.rancher.com/install-docker/20.10.sh | sh
usermod -aG docker ubuntu


sudo apt update -y
sudo apt install nodejs npm -y
sudo npm install -g vtop

docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

docker exec -it ollama ollama help

docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v ollama-webui:/app/backend/data --name ollama-webui --restart always ghcr.io/ollama-webui/ollama-webui:main

  
# Can you analyse applications logs and provide proper fixes?

docker exec -it ollama ollama run llama3
  # Muito bom
docker exec -it ollama ollama run llama3.2
  # Muito bom

docker exec -it ollama ollama run mistral-nemo
  # Excelente
  
docker exec -it ollama ollama run mistral


docker exec -it ollama ollama run mixtral # Muita CPU
# Error: model requires more system memory (27.7 GiB) than is available (14.3 GiB)


docker exec -it ollama ollama run gemma # Google 2b


http://18.219.127.251:3000/

vtop

```




Example of a prompt to analyse logs


```txt
You are a Senior DevOps Engineer and you are receiving a TOP 20 count from a ElasticSearch index, that one alert send wh reach over some thresold. May be logs are rising with applications not healthy, so, analyze this alert message, provide possible solutions for then and return usin less than 1900 characters, because Discord limit is this. Here is the  aler data for you to analyse and provide insights and fixes: 

[{'doc_count': 80, 'key': 'INFO: Logging large data: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa... (truncated)\n'}, {'doc_count': 79, 'key': 'CRITICAL: Critical log: System failure imminent.\n'}, {'doc_count': 79, 'key': 'DEBUG: Debug log message for troubleshooting.\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 0: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 100: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 101: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 102: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 103: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 104: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 105: Important data\n'}]
```



## 16. Test the model/models

https://github.com/ollama/ollama/blob/main/docs/api.md


18.217.0.238

```sh 

curl http://18.217.0.238:11434/api/chat -d '{
  "model": "mistral-nemo",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": false
}'


curl http://18.217.0.238:11434/api/chat -d '{
  "model": "mistral-nemo",
  "messages": [
    {
      "role": "user",
      "content": "Can you act a DevOps Engineer and analyze logs for me?"
    }
  ],
  "stream": false
}'



{"model":"llama3","created_at":"2024-10-27T22:09:16.827963042Z","message":{"role":"assistant","content":"What a great question!\n\nThe sky appears blue because of a phenomenon called scattering, which is the way that light interacts with tiny molecules of gases in the Earth's atmosphere. Here's what happens:\n\n1. **Sunlight enters the atmosphere**: When sunlight enters the Earth's atmosphere, it encounters tiny molecules of gases such as nitrogen (N2) and oxygen (O2).\n2. **Scattering occurs**: These gas molecules scatter the shorter, blue wavelengths of light more than the longer, red wavelengths. This is because the smaller molecules are better at interacting with the shorter wavelengths.\n3. **Blue light is dispersed**: As a result of this scattering, the blue light is dispersed throughout the atmosphere, reaching our eyes from all directions.\n4. **Red light continues straight**: The longer, red wavelengths of light continue to travel in a straight line, reaching our eyes only from directly overhead.\n5. **Our brain combines the colors**: When we look at the sky, our brain combines the blue light that's been scattered throughout the atmosphere with the red light that's come directly from the sun. This combination gives us the sensation of seeing a blue sky.\n\nIt's worth noting that the color of the sky can appear different under various conditions:\n\n* During sunrise and sunset, when the sun is lower in the sky, the light has to travel longer distances through more of the Earth's atmosphere. This means there are even more molecules scattering the shorter wavelengths, making the sky appear more reddish or orange.\n* On cloudy days, the clouds can scatter light in a way that makes the sky appear whiter or grayer.\n* In spaces with very little atmospheric gases, such as high-altitude planes or spacecraft, the sky may appear darker or blacker because there's less scattering of light.\n\nSo, to summarize: the sky appears blue because of the scattering of sunlight by tiny molecules in the Earth's atmosphere, which favors shorter wavelengths like blue and violet over longer wavelengths like red."},"done_reason":"stop","done":true,"total_duration":90998255290,"load_duration":21949114,"prompt_eval_count":16,"prompt_eval_duration":216358000,"eval_count":397,"eval_duration":90717787000}


curl http://18.118.130.152:11434/api/generate -d '{ "model": "mistral", "prompt": "What is water made of?" }'

curl http://13.59.251.54:11434/api/generate -d '{ "model": "llama2", "prompt": "What is water made of?" }'


curl http://13.59.251.54:11434/api/generate -d '{ "model": "gemma", "prompt": "What is water made of?" }'


ollama pull llama2

ollama rm llama3

ollama list


```


Example of a prompt to analyse logs


```txt
You are a Senior DevOps Engineer and you are receiving a TOP 20 count from a ElasticSearch index, that one alert send wh reach over some thresold. May be logs are rising with applications not healthy, so, analyze this alert message, provide possible solutions for then and return usin less than 1900 characters, because Discord limit is this. Here is the  aler data for you to analyse and provide insights and fixes: 

[{'doc_count': 80, 'key': 'INFO: Logging large data: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa... (truncated)\n'}, {'doc_count': 79, 'key': 'CRITICAL: Critical log: System failure imminent.\n'}, {'doc_count': 79, 'key': 'DEBUG: Debug log message for troubleshooting.\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 0: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 100: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 101: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 102: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 103: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 104: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 105: Important data\n'}]
```


# llama3


A TOP 20 count from ElasticSearch!

The alert indicates that the number of logs reaching a certain threshold. Let's break it down:

* 80% of logs are "INFO: Logging large data" (truncated), which might be normal or even expected.
* 79% of logs are "CRITICAL: System failure imminent", "DEBUG: Debug log message", and repeated "DEBUG: Repeated log X: Important data" messages. This suggests that there may be issues with the application(s) logging critical errors, debug messages, and potentially important data.

Possible solutions:

1. **Log analysis**: Investigate the logs to identify the root cause of the increased logging activity.
2. **Error tracking**: Set up error tracking tools (e.g., Sentry, Rollbar) to capture and analyze errors in real-time.
3. **Debugging**: Use debug logs to troubleshoot issues, but consider implementing log rotation or aggregation to reduce noise.
4. **Alert tuning**: Adjust the alert threshold to reduce false positives or missed critical events.

Remember, as a DevOps engineer, it's essential to monitor and analyze logs to identify potential issues before they become critical!





# llama3.2

The alert message suggests that the system is experiencing repeated debug log messages with "Important data" in them. This could be an indication of a problem or a misconfiguration.

Possible solutions:

1. **Filter out unnecessary logs**: Add a filter to only index logs with a certain severity level (e.g., INFO, WARNING) and exclude debug logs.
2. **Configure logging levels**: Adjust the logging levels for each module or component to reduce the number of debug logs generated.
3. **Implement logging throttling**: Use a logging library that allows for throttling or rate limiting to prevent excessive log messages from being generated.

These changes should help reduce the volume of logs and prevent the system from reaching the threshold.



# mixtral
Error: model requires more system memory (27.7 GiB) than is available (14.3 GiB)


# mistral-nemo

**Analysis:**
- `INFO` logs spiked (80), likely due to excessive data logging.
- `CRITICAL` alert triggered (79), indicating system failure risk.
- Multiple `DEBUG` logs repeated (79 each), suggesting potential infinite loops or stuck threads.

**Possible Solutions:**
1. **Tune ElasticSearch:** Adjust index patterns, slow logs, and increase query cache to reduce `INFO` logging.
2. **Investigate Critical Alert:** Review the critical log for root cause, possibly related to resource exhaustion (CPU/memory).
3. **Debug Repeated Logs:** Check for infinite loops or stuck threads in your application. Inspect methods called from repeated logs (`100-105`).
4. **Monitor & Alert:** Set up additional alerts for high `INFO` logs (>70) and frequent `DEBUG` logs (>50).

**Next Steps:**
- Gather more context: Check system resources, recent code changes, and application performance.
- Collaborate with developers to diagnose and fix issues causing excessive logging.


# mistral


 Based on the alert data provided, it appears that there are multiple issues affecting the system:

1. High volume of INFO level logs with large data (truncated in the example), which may indicate applications or services that are performing unnecessary operations, causing performance degradation and increased resource usage. Possible solutions could include optimizing application code to reduce log output or configuring ElasticSearch to handle large logs more efficiently.
2. Critical log messages indicating system failure imminent. This is a serious issue and requires immediate attention. It's recommended to investigate the root cause of this error, which may involve reviewing application or service logs for more details, restarting affected services, or potentially applying patches or updates.
3. A high number of DEBUG level log messages, particularly repeated ones with identical content. This can lead to excessive log clutter and make it difficult to identify important messages. To address this issue, consider filtering or suppressing unnecessary debug logs, configuring ElasticSearch to only index critical/error logs or using log rotation to manage large log files.
4. The high doc_count value of 79 suggests that there might be a problem with the logging infrastructure itself, as it appears to be ingesting the same log messages repeatedly. It's recommended to investigate this issue further and ensure that the logging pipeline is functioning correctly and not experiencing any errors or delays in processing logs.
5. The large number of repeated debug log messages (100-105) with identical content may indicate a recurring issue within the application or service, which should be investigated to identify and resolve the underlying problem.

Overall, it's important to address all these issues in order to improve system performance, stability, and maintainability. This might involve code optimizations, log filtering/suppression, troubleshooting critical errors, and ensuring logging infrastructure is functioning correctly.