resource "aws_vpc" "myhw__vpc" {
  cidr_block = "10.0.0.0/16"  # Example: 10.0.0.0/16
}

resource "aws_subnet" "myhw_public_subnet" {
  vpc_id                  = aws_vpc.myhw__vpc.id
  cidr_block              = "10.0.1.0/24" 
  map_public_ip_on_launch = true
  availability_zone        = "us-east-1a"  
}

resource "aws_subnet" "myhw_private_subnet" {
  vpc_id           = aws_vpc.myhw__vpc.id
  cidr_block       = "10.0.2.0/24"  
  availability_zone = "us-east-1a"  
}
