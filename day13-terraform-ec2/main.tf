terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-2"
}

# Dynamically fetch the latest Amazon Linux 2023 AMI instead of hardcoding one
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-*-x86_64"]
  }
}

resource "aws_security_group" "web_sg" {
  name        = "terraform-ssh-sg"
  description = "Allow SSH from my IP"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["70.80.144.47/32"]  # replace with your actual public IP
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "terraform-ssh-sg"
  }
}

resource "aws_instance" "my_server" {
  ami                    = data.aws_ami.amazon_linux.id
  instance_type          = "t3.micro"
  key_name               = "devops-journey-key"  # the key pair you already created on Day 8
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  tags = {
    Name = "terraform-managed-server"
  }
}

output "instance_public_ip" {
  value = aws_instance.my_server.public_ip
}
