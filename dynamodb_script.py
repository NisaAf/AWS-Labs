import boto3

# Initialize DynamoDB Client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

# Insert Data
table.put_item(Item={
    'StudentId': 'S002',  # Changed from 'StudentID' to 'StudentId'
    'Name': 'Jane Smith',
    'Age': 22,
    'Department': 'Mathematics'
})

# Retrieve Data
response = table.get_item(Key={'StudentId': 'S002'})  # Fixed typo 'StudentIdclec'
print(response['Item'])