import boto3

# Initialize DynamoDB Client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('User')

# Insert Data - User 1 (current)
table.put_item(Item={
    'UserID': 'user001',
    'Timestamp': 7000,  # Recent timestamp (within last 7 days)
    'Name': 'John Doe',
    'Email': 'john.doe@example.com',
    'LastLogin': '2023-04-09'
})
print("Inserted user001")

# Insert Data - User 2 (2 days ago)
table.put_item(Item={
    'UserID': 'user002',
    'Timestamp': 6000,  # Recent timestamp (within last 7 days)
    'Name': 'Jane Smith', 
    'Email': 'jane.smith@example.com',
    'LastLogin': '2023-04-07'
})
print("Inserted user002")

# Insert Data - User 3 (5 days ago)
table.put_item(Item={
    'UserID': 'user003',
    'Timestamp': 5000,  # Recent timestamp (within last 7 days)
    'Name': 'Robert Johnson',
    'Email': 'robert.johnson@example.com',
    'LastLogin': '2023-04-04'
})
print("Inserted user003")

# Insert Data - User 4 (8 days ago)
table.put_item(Item={
    'UserID': 'user004',
    'Timestamp': 2000,  # Older timestamp (more than 7 days ago)
    'Name': 'Sarah Williams',
    'Email': 'sarah.williams@example.com',
    'LastLogin': '2023-04-01'
})
print("Inserted user004")

# Insert Data - User 5 (10 days ago)
table.put_item(Item={
    'UserID': 'user005',
    'Timestamp': 1000,  # Oldest timestamp (more than 7 days ago)
    'Name': 'Michael Brown',
    'Email': 'michael.brown@example.com',
    'LastLogin': '2023-03-30'
})
print("Inserted user005")

# Retrieve Data for a specific user
response = table.get_item(Key={'UserID': 'user001', 'Timestamp': 7000})
print("\nRetrieved user001:")
print(response['Item'])

# Query users who logged in within the last 7 days (using Timestamp)
# For this example, we'll consider Timestamp values > 3000 as "within last 7 days"
cutoff_timestamp = 3000
print(f"\nQuerying users with Timestamp > {cutoff_timestamp} (last 7 days):")

# FIXED: Using ExpressionAttributeNames to handle reserved keyword "Timestamp"
response = table.scan(
    FilterExpression='#ts > :ts_value',
    ExpressionAttributeNames={
        '#ts': 'Timestamp'
    },
    ExpressionAttributeValues={
        ':ts_value': cutoff_timestamp
    }
)

# Display results
for user in response['Items']:
    print(f"UserID: {user['UserID']}, Name: {user['Name']}, Timestamp: {user['Timestamp']}")

print(f"\nTotal users active within last 7 days: {len(response['Items'])}")