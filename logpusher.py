import sys
import requests
import time
import secrets
import argparse

# This script is very simple. It does the equivalent of:
# curl -i -X POST http(s)://endpoint/v1/logs \
# -H "Content-Type: application/json" \
# -d @log.json

#############################################################################
# USAGE
# python logpusher.py -ep=http(s)://localhost:4318 --content "this is my log line"
#############################################################################

# Returns attributes list:
# From spec: https://opentelemetry.io/docs/concepts/signals/traces/#attributes
# Syntax: {
#           "key": "my.scope.attribute",
#           "value": {
#             "stringValue": "some scope attribute"
#           }
#         }
# Ref: https://github.com/open-telemetry/opentelemetry-proto/blob/9876ebfc5bcf629d1438d1cf1ee8a1a4ec21676c/examples/trace.json#L20-L56
# Values must be a non-null string, boolean, floating point value, integer, or an array of these values
# stringValue, boolValue, intValue, doubleValue, arrayValue, kvlistValue, bytesValue are all valid
def get_attributes_list(args):

    arg_list = []
    dropped_attribute_count = 0

    if args == None or len(args) < 1:
        return arg_list, dropped_attribute_count

    for item in args:
        # How many = are in the item?
        # 0 = invalid item. Ignore
        # 1 = key=value (logpusher assumes type=stringValue)
        # 2 = key=value=type (user is explicitly telling us the type. logpusher uses it)
        # >3 = invalid item. logpusher does not support span keys and value containing equals. Ignore.
        number_of_equals = item.count("=")
        if number_of_equals == 0 or number_of_equals > 2:
           dropped_attribute_count += 1
           continue

        key = ""
        value = ""
        type = "stringValue"

        if number_of_equals == 1:
            key, value = item.split("=", maxsplit=1)
            # User did not pass a type. Assuming type == 'stringValue'
        
        if number_of_equals == 2:
            key, value, type = item.split('=',maxsplit=2)
            # User passed an explicit type. Logpusher will use it.

        arg_list.append({"key": key, "value": { type: value}})
    
    return arg_list, dropped_attribute_count

parser = argparse.ArgumentParser()

# Notes:
# You can use either short or long (mix and match is OK)
# Hyphens are replaced with underscores hence for retrieval
# and leading hyphens are trimmed
# --span-name becomes args.span_name
# Retrieval also uses the second parameter
# Hence args.dry_run will work but args.d won't
parser.add_argument('-ep', '--endpoint', required=True)
parser.add_argument('-c', '--content', required=True)
parser.add_argument('-attrs', '--attributes', required=False, nargs='*')
parser.add_argument('-t', '--timestamp', required=False, default="")
parser.add_argument('-tid', '--trace-id', required=False, default=None)
parser.add_argument('-sid', '--span-id', required=False, default=None)
parser.add_argument('-tsd', '--time-shift', required=False, default="")
parser.add_argument('-dr','--dry-run','--dry', required=False, default="False")
parser.add_argument('-x', '--debug', required=False, default="False")
parser.add_argument('-insec', '--insecure', required=False, default="False")


args = parser.parse_args()

endpoint = args.endpoint
log_line = args.content
attributes = args.attributes
timestamp = args.timestamp
trace_id = args.trace_id
span_id = args.span_id
time_shift_duration = args.time_shift
dry_run = args.dry_run
debug_mode = args.debug
allow_insecure = args.insecure

# disable until v0.3.0
#if endpoint.startswith("http://") and not ALLOW_INSECURE:
#  print("ERROR: Endpoint is http:// (insecure). You MUST set '--insecure true'. Log line has NOT been sent.")
#  sys.exit(1)

attributes_list, dropped_attribute_count = get_attributes_list(args.attributes)

# Debug mode required?
DEBUG_MODE = False
if debug_mode.lower() == "true":
   print("> Debug mode is ON")
   DEBUG_MODE = True

DRY_RUN = False
if dry_run.lower() == "true":
   print("> Dry run mode is ON. Nothing will actually be sent.")
   DRY_RUN = True

# Prior to v0.3.0
# This flag will ONLY print a soft WARNING
# If the flag is False (explicitly or omitted)
# a warning is given that in v0.3.0 calls to http:// endpoints
# will FAIL if "--insecure true" is NOT set
#
# In other words, prior to v0.3.0 no breaking change
# v0.3.0 and above, if a user wishes to send to an http:// endpoint
# --insecure true MUST be set
#
# Best practice: Start setting this flag now!

# First convert to boolean
ALLOW_INSECURE = False
if allow_insecure.lower() == "true":
  ALLOW_INSECURE = True

# TODO: Adjust this error message for >=v0.3.0
# From v0.3.0 make this WARN only appear in DEBUG_MODE
if not ALLOW_INSECURE:
  print("WARN: --insecure flag is omitted or is set to false. Prior to v0.3.0 logpusher still works as expected (log is sent). In v0.3.0 and above, you MUST set '--insecure true' if you want to send to an http:// endpoint. See https://github.com/agardnerIT/logpusher/issues/18")

if DEBUG_MODE:
  print(f"Endpoint: {endpoint}")
  print(f"Log Line: {log_line}")
  print(f"Attributes: {attributes_list}")
  print(f"Timestamp: {timestamp}")
  print(f"Dry Run: {type(dry_run)} = {dry_run}")
  print(f"Debug: {type(debug_mode)} = {debug_mode}")
  print(f"Time Shift Duration (seconds): {time_shift_duration}")
  print(f"Trace ID: {trace_id}")
  print(f"Span ID: {span_id}")
  print(f"Allow insecure endpoints: {allow_insecure}")

# if user has not specified a timestamp
if timestamp == "":
   # get time now
   timestamp = time.time_ns()
else: # validate timestamp
    if len(timestamp) != 19:
        sys.exit("Error: timestamp must be a 19 digit number. Nanoseconds from unix epoch)")
    else: # try to parse from string to int
        try:
            timestamp = int(timestamp)
        except:
            sys.exit("Error: timestamp must be a 19 digit number. Nanoseconds from unix epoch)")

if time_shift_duration != "":
    try:
        time_shift_duration = int(time_shift_duration)
    except:
        sys.exit("Error: time_shift_duration must be specified as a number of seconds (eg. 2)")

    # time_shift_duration is expected to be in seconds
    # convert to nano seconds
    duration = time_shift_duration * 1000000000
    timestamp = timestamp - duration

# cast time_now to string
# This is required by spec
timestamp = str(timestamp)

if DEBUG_MODE and trace_id is not None:
    if len(trace_id) != 32:
        print(f"Warning: Trace ID is too short ({len(trace_id)} characters). Collector will fail to accept it.")
    else:
        print("Trace ID is of the correct length (32 characters). Collector will accept it.")
    
if DEBUG_MODE and span_id is not None:
    if len(span_id) != 16:
        print(f"Warning: Span ID is too short ({len(span_id)} characters). Collector will fail to accept it.")
    else:
        print("Span ID is of the correct length (16 characters). Collector will accept it.")

log = {
	"resourceLogs": [{
		"resource": {
			"attributes": []
		},
		"scopeLogs": [{
			"scope": {},
			"logRecords": [{
				"timeUnixNano": timestamp,
				"body": {
					"stringValue": log_line
				},
				"attributes": attributes_list,
				"droppedAttributesCount": dropped_attribute_count,
				"traceId": trace_id,
				"spanId": span_id
			}]
		}]
	}]
}

if DEBUG_MODE:
   print(f"Collector Endpoint: {endpoint}. Log JSON: {log}")

if not DRY_RUN:
  resp = requests.post(f"{endpoint}/v1/logs", headers={ "Content-Type": "application/json" }, json=log, timeout=5)
  print(resp)
