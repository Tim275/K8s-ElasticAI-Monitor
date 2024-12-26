elastic-watcher.md


```sh
PUT _watcher/watch/log_threshold_watch
{
  "trigger": {
    "schedule": {
      "interval": "3m"
    }
  },
  "input": {
    "search": {
      "request": {
        "indices": ["k8s-infra*"],
        "body": {
          "query": {
            "range": {
              "@timestamp": {
                "gte": "now-30m",
                "lt": "now"
              }
            }
          },
          "aggs": {
            "duplicate_logs": {
              "terms": {
                "field": "log.keyword",
                "size": 20,
                "min_doc_count": 2
              }
            }
          }
        }
      }
    }
  },
  "condition": {
    "script": {
      "source": "return ctx.payload.aggregations.duplicate_logs.buckets.size() > 0"
    }
  },
  "actions": {
    "send_to_webhook": {
      "webhook": {
        "method": "POST",
        "url": "http://3.140.193.119:5000/alert",
        "body": "{{#toJson}}ctx.payload.aggregations.duplicate_logs.buckets{{/toJson}}",
        "headers": {
          "Content-Type": "application/json"
        }
      }
    }
  }
}


# Activate
PUT _watcher/watch/log_threshold_watch/_activate

# Test the wather
POST _watcher/watch/log_threshold_watch/_execute


# Monitor e alerting
GET _watcher/stats/active_watches

GET .watcher-history*/_search?q=watch_id:log_threshold_watch

```



RESULT RECEIVED IN THE API - 

```sh

INFO:main:Received alert: [{'doc_count': 20, 'key': 'DEBUG: Debug log message for troubleshooting.\n'}, {'doc_count': 20, 'key': 'INFO: Frequent log message 993\n'}, {'doc_count': 20, 'key': 'INFO: Frequent log message 994\n'}, {'doc_count': 20, 'key': 'INFO: Frequent log message 995\n'}, {'doc_count': 20, 'key': 'INFO: Frequent log message 996\n'}, {'doc_count': 20, 'key': 'INFO: Frequent log message 997\n'}, {'doc_count': 20, 'key': 'INFO: Frequent log message 998\n'}, {'doc_count': 20, 'key': 'INFO: Frequent log message 999\n'}, {'doc_count': 20, 'key': 'INFO: Info log message with some useful info.\n'}, {'doc_count': 19, 'key': 'CRITICAL: Critical log: System failure imminent.\n'}]
INFO:werkzeug:20.115.71.174 - - [26/Oct/2024 17:34:56] "POST /alert HTTP/1.1" 200 -
INFO:main:Received alert: [{'doc_count': 49, 'key': 'DEBUG: Repeated log 0: Important data\n'}, {'doc_count': 49, 'key': 'DEBUG: Repeated log 100: Important data\n'}, {'doc_count': 49, 'key': 'DEBUG: Repeated log 101: Important data\n'}, {'doc_count': 49, 'key': 'DEBUG: Repeated log 102: Important data\n'}, {'doc_count': 49, 'key': 'DEBUG: Repeated log 103: Important data\n'}, {'doc_count': 49, 'key': 'DEBUG: Repeated log 104: Important data\n'}, {'doc_count': 49, 'key': 'DEBUG: Repeated log 105: Important data\n'}, {'doc_count': 49, 'key': 'DEBUG: Repeated log 106: Important data\n'}, {'doc_count': 49, 'key': 'DEBUG: Repeated log 107: Important data\n'}, {'doc_count': 49, 'key': 'DEBUG: Repeated log 108: Important data\n'}]
INFO:werkzeug:20.115.71.174 - - [26/Oct/2024 17:37:55] "POST /alert HTTP/1.1" 200 -
INFO:main:Received alert: [{'doc_count': 80, 'key': 'INFO: Logging large data: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa... (truncated)\n'}, {'doc_count': 79, 'key': 'CRITICAL: Critical log: System failure imminent.\n'}, {'doc_count': 79, 'key': 'DEBUG: Debug log message for troubleshooting.\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 0: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 100: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 101: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 102: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 103: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 104: Important data\n'}, {'doc_count': 79, 'key': 'DEBUG: Repeated log 105: Important data\n'}]

```
