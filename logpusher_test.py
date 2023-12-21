import pytest
import subprocess

def run_logpusher(args=""):
    output = subprocess.run(f"python3 logpusher.py {args}" , capture_output=True, shell=True, text=True)
    return output

# Run logpusher with no input params
# Should error and so check error is present
def test_run_no_params():
    output = run_logpusher()
    assert output.returncode > 0
    assert output.stderr != ""
    assert "error" in output.stderr

def test_check_debug_mode():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Debug mode is ON" in output.stdout

def test_check_dry_run_mode():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Dry run mode is ON" in output.stdout

def test_check_collector_url():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Endpoint: http://otelcollector:4317" in output.stdout

def test_check_log_line_output():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Log Line: This is a log line" in output.stdout

def test_check_attributes_output():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --attributes foo=bar foo2=bar2=stringValue foo3=123=intValue --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Attributes: [{'key': 'foo', 'value': {'stringValue': 'bar'}}, {'key': 'foo2', 'value': {'stringValue': 'bar2'}}, {'key': 'foo3', 'value': {'intValue': '123'}}]" in output.stdout

def test_trace_id_output():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --trace-id abcd1234  --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Trace ID: abcd1234" in output.stdout

def test_span_id_output():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --span-id abcd1234  --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Span ID: abcd1234" in output.stdout

# Broken
# https://github.com/agardnerIT/logpusher/issues/19
# TODO: Fix and re-enable test
# def test_check_time_shift_output():
#     args = "-ep http://otelcollector:4317 -c 'This is a log line' --time-shift 2 --dry-run true --debug true"
#     output = run_logpusher(args)
#     assert output.returncode == 0
#     assert "Time Shift Duration (seconds): 20" in output.stdout
    