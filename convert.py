import json
import sys
from datetime import datetime, timedelta

def convert_unix_to_gmt_530(unix_timestamp):
    # Convert Unix timestamp to datetime
    timestamp = datetime.utcfromtimestamp(unix_timestamp)
    # Add 5 hours and 30 minutes to convert to GMT+5:30
    gmt_530_time = timestamp + timedelta(hours=5, minutes=30)
    return gmt_530_time.strftime('%Y-%m-%d %H:%M:%S')

# Read the Unix timestamp from the command line arguments
input_timestamp = int(sys.argv[1])

# Perform the conversion
converted_time = convert_unix_to_gmt_530(input_timestamp)

# Output the result as JSON
print(json.dumps({"converted_time": converted_time}))
