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


def test_check_timestamp_output():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --timestamp 1234567890123456789 --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Timestamp: 1234567890123456789" in output.stdout

def test_validate_failure_for_invalid_timestamp_length():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --timestamp 1234 --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode != 0
    assert "Timestamp: 1234" in output.stdout # should still be present in debug
    assert "Error: timestamp must be a 19 digit number. Nanoseconds from unix epoch)" in output.stderr

# timestamp must be a 19 digit int
# So anything else should fail
def test_validate_failure_for_invalid_timestamp_format():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --timestamp '01/01/2023 10:00:00' --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode != 0
    assert "Timestamp: 01/01/2023 10:00:00" in output.stdout # should still be present in debug
    assert "Error: timestamp must be a 19 digit number. Nanoseconds from unix epoch)" in output.stderr

def test_check_attributes_output():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --attributes foo=bar foo2=bar2=stringValue foo3=123=intValue --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Attributes: [{'key': 'foo', 'value': {'stringValue': 'bar'}}, {'key': 'foo2', 'value': {'stringValue': 'bar2'}}, {'key': 'foo3', 'value': {'intValue': '123'}}]" in output.stdout

def test_without_trace_id():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Trace ID: None" in output.stdout

def test_trace_id_too_short_output():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --trace-id abcd1234  --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Trace ID: abcd1234" in output.stdout
    assert "Warning: Trace ID is too short" in output.stdout

def test_without_span_id():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Span ID: None" in output.stdout

def test_span_id_too_short_output():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --span-id abcd1234  --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Span ID: abcd1234" in output.stdout
    assert "Warning: Span ID is too short" in output.stdout

# Broken
# https://github.com/agardnerIT/logpusher/issues/19
def test_check_time_shift_output():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --time-shift 2 --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode == 0
    assert "Time Shift Duration (seconds): 2" in output.stdout

def test_validate_failure_for_invalid_time_shift_duration():
    args = "-ep http://otelcollector:4317 -c 'This is a log line' --time-shift 2s --dry-run true --debug true"
    output = run_logpusher(args)
    assert output.returncode != 0
    assert "Error: time_shift_duration must be specified as a number of seconds (eg. 2)" in output.stderr

# Check that --allow-insecure false
# When flag is omitted
# Also check that WARN message
# TODO: Revisit this for v0.3.0
def test_check_insecure_flag_false_when_unset():    
   args = "-ep http://otelcollector:4317 -c 'This is a log line' --dry-run true --debug true"
   output = run_logpusher(args)
   assert output.returncode == 0
   assert "allow insecure endpoints: false" or "" in output.stdout.lower()
   #assert "WARN: --insecure flag is omitted or is set to false. Prior to v0.3.0 logpusher still works as expected (log is sent). In v0.3.0 and above, you MUST set '--insecure true' if you want to send to an http:// endpoint. See https://github.com/agardnerIT/logpusher/issues/78" in output.stdout

# Check that --allow-insecure flag false
# When flag is explicitly set
# TODO: Revisit this for v0.3.0
def test_check_insecure_flag_false_when_set():
   args = "-ep http://otelcollector:4317 -c 'This is a log line' --dry-run true --debug true --insecure false"
   output = run_logpusher(args)
   assert output.returncode == 0
   assert "allow insecure endpoints: false" in output.stdout.lower()
   assert "WARN: --insecure flag is omitted or is set to false. Prior to v0.3.0 logpusher still works as expected (log is sent). In v0.3.0 and above, you MUST set '--insecure true' if you want to send to an http:// endpoint. See https://github.com/agardnerIT/logpusher/issues/18" in output.stdout

# Check that --allow-insecure flag false
# When flag is explicitly set
# TODO: Revisit this for v0.3.0
def test_check_insecure_flag_true_when_set():
   args = "-ep http://otelcollector:4317 -c 'This is a log line' --dry-run true --debug true --insecure True"
   output = run_logpusher(args)
   assert output.returncode == 0
   assert "allow insecure endpoints: true" in output.stdout.lower()
    