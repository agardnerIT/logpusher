## Timestamp

The optional `-t` parameter, or the equivalent long form version `--timestamp` makes is possible for to specify a custom log timestamp. If not set, logpusher sets the log timestamp as `now`.

### Timestamp Format
The `-t` or `--timestamp` parameter is expected in nanoseconds of time since the unix epoch. Hint: Grab the value from [this website](https://www.unixtimestamp.com) then add 9 zeros.

For example `1687169964000000000`