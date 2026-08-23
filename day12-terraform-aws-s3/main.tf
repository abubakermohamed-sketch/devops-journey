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

resource "aws_s3_bucket" "my_bucket" {
  bucket = "mohamed-devops-journey-2026"  # must be globally unique across ALL AWS accounts

  tags = {
    Name        = "devops-journey-bucket"
    Environment = "learning"
    ManagedBy   = "terraform"
  }
}
