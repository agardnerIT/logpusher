## Insecure Flag

> Introduced in v0.2.0

Default: `false`

The optional `-ins [false|true]` or `--insecure [false|true]` flag exists to encourage "secure by default" practices by encouraging the sending of span only to `https://` endpoints. However, logpusher **does** still work with `http://` endpoints.

The `--insecure` flag affects whether or not logpusher will connect to insecure `http://` endpoints or not.

The `--insecure` flag operation differs by version.

### v0.1.*

The `--insecure` is not available

### v0.2.*

The `--insecure` flag defaults to `false` with the intention of meaning insecure endpoints are not allowed. However, to provide ample migration time for end users, the behaviour is as follows:

- `--insecure` flag is omitted

  This is the expected behaviour of everyone migrating from v0.1 to v0.2.
  The flag defaults to `false` BUT will still allow `http://` endpoints, just like before.
  
  Logpusher will emit a soft `WARNING` message to inform users of the upcoming breaking change, like this:

  ```
  WARN: --insecure flag is omitted or is set to false. Prior to v0.3.0 logpusher still works as expected (span is sent). In v0.3.0 and above, you MUST set '--insecure true' if you want to send to an http:// endpoint. See https://github.com/agardnerIT/logpusher/issues/18
  ```

- `--insecure` flag is explicitly set to false

  From v0.3 upwards, users are encouraged to get into the best practice habit of explicitly setting this to `false` or `true`.

  Otherwise, for v0.2.*, the behaviour is as above.

### v0.3

If the `--insecure` flag is omitted or explicitly set to `false`, calls to `http://` endpoints will be `BLOCKED`.

Calls to `http://` endpoints MUST be accompanied with the `--insecure true` flag or calls will be blocked with this error:

```
ERROR: Endpoint is http:// (insecure). You MUST set '--insecure true'. Log has NOT been sent.
```

