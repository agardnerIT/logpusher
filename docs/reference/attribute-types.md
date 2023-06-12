## Attribute Types

The optional `-attrs` or equivalent long form version: `--attributes` exists to add attributes to the logs that logpusher creates.

Add as many attributes as you like.

### Formatting Attributes

Tracepusher will accept two possible inputs:

- `--attributes foo=bar`
- `--attributes foo=bar=<TYPE>`

In the first, the value is assumed to be of type `stringValue`.

In the second, **you** specify the value type. Possible types are: `stringValue`, `boolValue`, `intValue`, `doubleValue`, `arrayValue`, `kvlistValue` or `bytesValue`.

Separate each attribute with a space.

```
python logpusher.py \
--endpoint http(s)://OTEL-COLLECTOR-ENDPOINT:4318 \
--content "This is my log line" \
--attributes foo=bar foo2=23=intValue
```

```
docker run gardnera/logpusher:v0.1.0 \
-ep http(s)://OTEL-COLLECTOR-ENDPOINT:4318 \
--content "This is my log line" \
-spnattrs foo=bar foo2=bar2=stringValue
```

### Valid Types

The following are all valid:

- `stringValue`
- `boolValue`
- `intValue`
- `doubleValue`
- `arrayValue`
- `kvlistValue`
- `bytesValue`