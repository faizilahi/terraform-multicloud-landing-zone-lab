# TEACHING ONLY — never apply without explicit sandbox credentials policy
terraform {
  required_version = ">= 1.5.0"
}

variable "environment" {
  type        = string
  description = "Label for teaching stacks"
  default     = "lab"
}

variable "cidr_block" {
  type    = string
  default = "10.10.0.0/16"
}

resource "aws_vpc" "landing" {
  cidr_block           = var.cidr_block
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name        = "landing-${var.environment}"
    Owner       = "Faiz Elahi"
    Purpose     = "Educational skeleton"
    DoNotApply  = "true-unless-sandbox"
  }
}

resource "aws_s3_bucket" "landing_logs" {
  bucket = "faiz-elahi-lz-logs-${var.environment}-teaching-placeholder"
  tags = {
    Purpose = "Storage placeholder — name must be globally unique if applied"
  }
}

output "vpc_id" {
  value = aws_vpc.landing.id
}
