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

# Prepare data for tabulation
table_data = []

for result in response['ResultsByTime']:
    start_date = result['TimePeriod']['Start']
    end_date = result['TimePeriod']['End']
    cost_amount = result['Total']['BlendedCost']['Amount']
    cost_unit = result['Total']['BlendedCost']['Unit']
    
    # Add row to the table
    table_data.append([start_date, end_date, cost_amount, cost_unit])

# Define the table headers
headers = ['Start Date', 'End Date', 'Cost Amount', 'Cost Unit']

# Print the table
print(tabulate(table_data, headers=headers, tablefmt='pretty'))
