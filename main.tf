terraform {
  backend "s3" {
    bucket         = "terraform-state-hw1"
    key            = "terraform/state.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}
provider "aws" {
  region = "us-east-1"  # Use the same region as your S3 bucket
}

resource "aws_instance" "example" {
  ami           = "ami-00a929b66ed6e0de6"  # Replace with an appropriate AMI ID for your region
  instance_type = "t2.micro"
  tags = {
    Name = "Terraform-Test-Instance"
  }
}