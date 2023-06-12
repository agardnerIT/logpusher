## Correlating Logs to Traces

Log entries sent by logpusher can be correlated with any OpenTelemetry spans / traces (if you need an easy way to generate spans and traces, try [tracepusher](https://agardnerit.github.io/tracepusher)).

## Adding Trace ID and Span ID

Your OpenTelemetry platform of choice needs two pieces of information to tie the log line to the span:

1. The span ID
2. The trace ID

These are added as additional commands when you use logpusher:

```
python logpusher.py \
  --endpoint http(s)://OTEL-COLLECTOR-ENDPOINT:4318 \
  --content "This is my log line" \
  --trace-id "TRACE-ID-GOES-HERE" \
  --span-id "SPAN-ID-GOES-HERE"
```