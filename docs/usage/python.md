## Requirements and Prequisites
- A running OpenTelemetry collector (see below)
- Python + Requests module

## Basic Python Usage

`python3 logpusher.py -h` or `python3 logpusher.py --help` shows help text.

```
python logpusher.py \
--endpoint http(s)://OTEL-COLLECTOR-ENDPOINT:4318 \
--content "A log line here"
```

### Optional Parameters

```
--attributes key=value [key2=value2...]
--timestamp <timeUnixNanos> eg. 1686545492000000000
--time-shift <seconds to shift log time backwards eg. 2>
--trace-id <32 character hex id>
--span-id <16 character hex id>
--dry-run true|false
--debug true|false
--insecure true| false
```

For attributes, see [Attributes](../reference/attribute-types.md).

For the timestamp parameter, see [timestamp](../reference/timestamp.md)

For time shifting, see [time shifting](../reference/time-shift.md)

To correlate log lines to traces, see [correlating logs to traces](../reference/correlating-logs-to-traces.md)

For dry run mode, see [dry run mode](../reference/dry-run-mode.md)

For debug mode, see [debug mode](../reference/debug-mode.md)

For the `insecure` flag, see [insecure flag](../reference/insecure-flag.md)

For information on span attributes and span attribute types, see [Span Attribute Types](../reference/span-attribute-types.md).

For multi-span traces, see [multi span traces](../reference/multi-span-traces.md)