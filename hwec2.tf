# Create EC2 instance configured as a web server in the private subnet
resource "aws_instance" "web_server" {
  ami                    = "ami-00a929b66ed6e0de6"  # Amazon Linux 2 in us-east-1
  instance_type          = "t2.micro"
  subnet_id              = "subnet-0e6026122e408dd43"  # Your private subnet
  vpc_security_group_ids = ["sg-0f6b0e8560b17510a"]  # Note the square brackets here
  key_name               = "is698"
  
  # User data to install and configure a web server
  user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo '<html><body><h1>Web Server in Private Subnet</h1><p>Created with Terraform</p></body></html>' > /var/www/html/index.html
    
    # Install AWS CLI to interact with S3
    yum install -y aws-cli
  EOF
  
  tags = {
    Name = "PrivateWebServer"
  }
}