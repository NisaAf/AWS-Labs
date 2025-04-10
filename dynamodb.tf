# Create DynamoDB table for storing user login details
resource "aws_dynamodb_table" "user_logins" {
  name         = "UserLoginDetails"
  billing_mode = "PAY_PER_REQUEST"  # On-demand capacity mode
  hash_key     = "UserID"           # Primary/Partition key
  range_key    = "Timestamp"        # Sort key
  
  # Define attributes for the keys
  attribute {
    name = "UserID"
    type = "S"  # String type
  }
  
  attribute {
    name = "Timestamp"
    type = "N"  # Number type
  }
  
  tags = {
    Name = "UserLoginDetails"
  }
}