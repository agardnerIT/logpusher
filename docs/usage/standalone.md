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
--insecure true|false
```

For documentation on all available flags, see the [reference pages](../reference/index.md)
