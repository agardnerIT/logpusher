# OpenTelemetry logpusher
Push OpenTelemetry log lines easily to a collector.

![logpusher architecture](./assets/architecture.png)

# Watch: logpusher in Action
TODO: [YouTube: logpusher](https://www.youtube.com/watch?v=TODO).

# Uses

- Push OpenTelemetry compatible logs from any script, pipeline or process
- [Correlate log entries with OpenTelemetry traces](https://agardnerit.github.io/tracepusher/reference/correlating-logs-to-traces)

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

See [try logpusher in-browser without installation](https://agardnerit.github.io/logpusher/try/).

## Python3 Usage

See [use logpusher as a Python script](https://agardnerit.github.io/logpusher/usage/python).


## Docker Usage

See [use logpusher as a docker image](https://agardnerit.github.io/logpusher/usage/python/).

## CI Usage

See [run a CI pipeline step as a docker image with logpusher](https://agardnerit.github.io/logpusher/usage/ci).

## Dry Run Mode

See [dry run mode flag](https://agardnerit.github.io/tracepusher/reference/dry-run-mode/).

## Debug Mode

See [debug mode flag](https://agardnerit.github.io/tracepusher/reference/debug-mode/).

## Time Shifting

See [time shifting](https://agardnerit.github.io/tracepusher/reference/time-shifting/).

## Log Attributes

See [log attribute types](https://agardnerit.github.io/tracepusher/reference/attribute-types/)

## Spin up OpenTelemetry Collector

See [OpenTelemetry Collector configuration](https://agardnerit.github.io/logpusher/reference/otel-col)

# Adopters

Do you use logpusher? Thanks and we'd love to know!

Submit a PR and add your details to [ADOPTERS.md](ADOPTERS.md)

# FAQs

See [FAQ](https://agardnerit.github.io/logpusher/faq).

# Breaking Changes

See [Breaking changes](https://agardnerit.github.io/logpusher/breaking-changes)

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

