import boto3
from tabulate import tabulate

# Initialize a boto3 client for the cost explorer service
ce_client = boto3.client('ce', region_name='us-east-1')

# Define the time range for the query
time_period = {
    'Start': '2025-02-01',
    'End': '2025-02-26'
}

# Get cost data
response = ce_client.get_cost_and_usage(
    TimePeriod=time_period,
    Granularity='DAILY',  # Can be 'DAILY', 'MONTHLY', etc.
    Metrics=['BlendedCost']
)

# Print the response
for result in response['ResultsByTime']:
    print(f"Start: {result['TimePeriod']['Start']}, End: {result['TimePeriod']['End']}")
    print(f"Total Cost: {result['Total']['BlendedCost']['Amount']} {result['Total']['BlendedCost']['Unit']}")
