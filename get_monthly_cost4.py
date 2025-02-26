import boto3
from tabulate import tabulate
import configparser

# List of AWS profiles in the credentials file
profiles = ['petpal', 'concati']  # List all your profiles here

# Function to get cost data for each account
def get_cost(profile_name):
    # Initialize a boto3 session using a specific profile
    session = boto3.Session(profile_name=profile_name)
    ce_client = session.client('ce', region_name='us-east-1')

    # Define the time range for the query (e.g., current month)
    time_period = {
        'Start': '2025-02-01',
        'End': '2025-02-28'
    }

    # Get cost data
    response = ce_client.get_cost_and_usage(
        TimePeriod=time_period,
        Granularity='MONTHLY',  # You can use 'DAILY' as well
        Metrics=['BlendedCost']
    )

    # Prepare data for tabulation
    table_data = []
    for result in response['ResultsByTime']:
        start_date = result['TimePeriod']['Start']
        end_date = result['TimePeriod']['End']
        cost_amount = result['Total']['BlendedCost']['Amount']
        cost_unit = result['Total']['BlendedCost']['Unit']
        table_data.append([profile_name, start_date, end_date, cost_amount, cost_unit])

    return table_data

# Collect data from all accounts
all_table_data = []

for profile in profiles:
    all_table_data.extend(get_cost(profile))

# Define headers for the table
headers = ['Account', 'Start Date', 'End Date', 'Cost Amount', 'Cost Unit']

# Print the results in a tabular format
print(tabulate(all_table_data, headers=headers, tablefmt='pretty'))
