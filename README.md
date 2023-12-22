# logpusher
Push OpenTelemetry log lines easily to a collector.

![logpusher architecture](./assets/architecture.png)

## [> View the logpusher documentation <](https://agardnerit.github.io/logpusher)

Want to do this with OpenTelemetry traces? Try [tracepusher](http://agardnerit.github.io/tracepusher/). Better still, use them together to correlate logs and traces.

# Watch: logpusher in Action
[YouTube: logpusher in action with Grafana & Loki](https://www.youtube.com/watch?v=-z6THmR_jvQ).

# Uses

- Push OpenTelemetry compatible logs from any script, pipeline or process
- [Correlate log entries with OpenTelemetry traces](https://agardnerit.github.io/logpusher/reference/correlating-logs-to-traces)

# Try In Browser

See [try logpusher in-browser without installation](https://agardnerit.github.io/logpusher/try/).

## Python3 Usage

See [use logpusher as a Python script](https://agardnerit.github.io/logpusher/usage/python).


## Docker Usage

See [use logpusher as a docker image](https://agardnerit.github.io/logpusher/usage/python/).

## CI Usage

See [run a CI pipeline step as a docker image with logpusher](https://agardnerit.github.io/logpusher/usage/ci).

## Dry Run Mode

See [dry run mode flag](https://agardnerit.github.io/logpusher/reference/dry-run-mode/).

## Debug Mode

See [debug mode flag](https://agardnerit.github.io/logpusher/reference/debug-mode/).

## Time Shifting

See [time shifting](https://agardnerit.github.io/logpusher/reference/time-shifting/).

## Log Attributes

See [log attribute types](https://agardnerit.github.io/logpusher/reference/attribute-types/)

## Insecure Mode

See [the insecure flag](https://agardnerit.github.io/logpusher/reference/insecure-flag/)

## Spin up OpenTelemetry Collector

See [OpenTelemetry Collector configuration](https://agardnerit.github.io/logpusher/reference/otel-col)

# Adopters

Do you use logpusher? Thanks and we'd love to know!

Submit a PR and add your details to [ADOPTERS.md](ADOPTERS.md)

# FAQs

See [FAQ](https://agardnerit.github.io/logpusher/faq).

# Breaking Changes

See [Breaking changes](https://agardnerit.github.io/logpusher/breaking-changes)

# Building Standalone Binaries

Note: PyInstaller is platform dependent. You must build on whatever platform you wish to run logpusher on.

When logpusher is released, the [build_standalone_binaries.yml workflow](.github/workflows/build_standalone_binaries.yml) completes this step and uploads the resulting binaries to S3 where we (currently manually) attach each generated binary to the release notes.

```
python -m PyInstaller --onefile logpusher.py
```

# Building Docker Image

Run all build commands from the root directory:

```
docker buildx build --platform linux/arm64,linux/amd64 --push -t logpusher:dev-ci -f ./docker/ci/Dockerfile .
docker buildx build --platform linux/arm64,linux/amd64 --push -t logpusher:dev -f ./docker/standard/Dockerfile .
```

# Testing

Run the test suite:

```
pytest
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

