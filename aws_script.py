import boto3
from datetime import datetime

# Initialize clients
s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')

# 1. List all files in a specified S3 bucket
bucket_name = 'my-hw3s3bucket-is698'  # Replace with your bucket name
print(f"Listing files in bucket: {bucket_name}")

response = s3.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response:
    for item in response['Contents']:
        print(f"- {item['Key']}")
else:
    print("No files found in bucket")

# 2. Create a DynamoDB table with ID, Name, and Department
table_name = 'Employees'
print(f"\nCreating DynamoDB table: {table_name}")

try:
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'ID', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'ID', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print(f"Table {table_name} created successfully")
except dynamodb.exceptions.ResourceInUseException:
    print(f"Table {table_name} already exists")

# Wait for table to be active
waiter = dynamodb.get_waiter('table_exists')
waiter.wait(TableName=table_name)

# 3. Insert an employee item into the DynamoDB table
print("\nInserting employee into DynamoDB table")

# Create an employee item
employee = {
    'ID': {'S': 'E001'},
    'Name': {'S': 'John Doe'},
    'Department': {'S': 'IT'}
}

# Insert the item
dynamodb.put_item(
    TableName=table_name,
    Item=employee
)

print("Employee added successfully")