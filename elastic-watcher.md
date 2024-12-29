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
        "url": "http://3.67.174.254:5000/alert",
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
