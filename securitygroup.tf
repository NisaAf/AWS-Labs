# Create security group for the web server
resource "aws_security_group" "web_server_sg" {
  name        = "web_server_sg"
  description = "Security group for web server in private subnet"
  vpc_id      = "vpc-04269a933172e72f5"  # Replace with your VPC ID

  # Allow HTTP from anywhere within the VPC
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]  # Replace with your VPC CIDR block
    description = "Allow HTTP from within VPC"
  }

  # Allow SSH from public subnet
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.1.0/24"]  # Replace with your public subnet CIDR
    description = "Allow SSH from public subnet"
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow all outbound traffic"
  }

  tags = {
    Name = "WebServerSG"
  }
}