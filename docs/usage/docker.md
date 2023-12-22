# Requirements and Prequisites
- A running OpenTelemetry collector (see below)
- Docker

## Basic Docker Usage

```
docker run gardnera/logpusher:v0.1.0 \
-ep http(s)://OTEL-COLLECTOR-ENDPOINT:4318 \
-c "This is my log line"
```

### Optional Parameters

```
--attributes key=value key2=value2=type
--timestamp <timeUnixNanos> eg. 1686545492000000000
--time-shift <seconds to shift log time backwards eg. 2>
--trace-id <32 character hex id>
--span-id <16 character hex id>
--dry-run true|false
--debug true|false
--insecure true| false
```

For attribute types, see [Attribute Types](../reference/attribute-types.md).

To correlate log lines to traces, see [correlating logs to traces](../reference/correlating-logs-to-traces.md)
