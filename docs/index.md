# OpenTelemetry logpusher
Push OpenTelemetry log lines easily to a collector.

![logpusher architecture](./assets/architecture.png)

# Watch: logpusher in Action
TODO: [YouTube: logpusher](https://www.youtube.com/watch?v=TODO).

# Uses

- Push OpenTelemetry compatible logs from any script, pipeline or process
- [Correlate log entries with OpenTelemetry traces](reference/correlating-logs-to-traces.md)

## Try Logpusher
See [try logpusher](try.md)

## Quick Start

```
docker run gardnera/logpusher:v0.1.0 \
  --endpoint http(s)://COLLECTOR-URL:4318 \
  --content "This is my log line"
```

## Advanced Usage
- [Correlating Logs to OpenTelemetry Traces](reference/correlating-logs-to-traces.md)
- [Docker usage](usage/docker.md)
- [Python usage](usage/python.md)
- [CI usage](usage/ci.md)
- [Log Attributes](reference/attribute-types.md)
- [logpusher reference page](reference/index.md)


# Try In Browser

See [try logpusher in-browser without installation](try.md).

## Python3 Usage

See [use logpusher as a Python script](usage/python.md).


## Docker Usage

See [use logpusher as a docker image](usage/docker.md).

## CI Usage

See [run a CI pipeline step as a docker image with logpusher](usage/ci.md).

## Dry Run Mode

See [dry run mode flag](reference/dry-run-mode.md).

## Debug Mode

See [debug mode flag](reference/debug-mode.md).

## Time Shifting

See [time shifting](reference/time-shift.md).

## Log Attributes

See [log attribute types](reference/attribute-types.md)

## Spin up OpenTelemetry Collector

See [OpenTelemetry Collector configuration](reference/otel-col.md)

# Adopters

Do you use logpusher? Thanks and we'd love to know!

Submit a PR and add your details to [ADOPTERS.md](ADOPTERS.md)

# FAQs

See [FAQ](faq.md).

# Breaking Changes

See [Breaking changes](breaking-changes.md)

# Building

Run all build commands from the root directory:

```
docker buildx build --platform linux/arm64,linux/amd64 --push -t logpusher:dev-ci -f ./docker/ci/Dockerfile .
docker buildx build --platform linux/arm64,linux/amd64 --push -t logpusher:dev -f ./docker/standard/Dockerfile .
```

----------------------

# Contributing

All contributions are most welcome!

Get involved:
- Tackle a [good first issue](https://github.com/agardnerIT/logpusher/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)
- Create an issue to suggest something new
- File a PR to fix something

<a href="https://github.com/agardnerit/logpusher/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=agardnerit/logpusher" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

