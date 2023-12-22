# Download binary

Download the relevant binary from the [GitHub releases page](https://github.com/agardnerit/logpusher/releases/latest).

## Run logpusher

```
./logpusher \
  -ep http(s)://OTEL-COLLECTOR-ENDPOINT:4318 \
  -c 'this is a log line'
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

For span atttribute types, see [Span Attribute Types](../reference/span-attribute-types.md).

For span events, see [Span events](../reference/span-events.md)

For multi-span traces, see [multi span traces](../reference/multi-span-traces.md)

For duration type, see [duration type](../reference/duration-type.md)

For span kind, see [span kind](../reference/span-kind.md)