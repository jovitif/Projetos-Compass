variable "aws_region" {
  description = "The AWS region to create resources in."
  type        = string
}

variable "vpc_cidr" {
  description = "The CIDR block for the VPC."
  type        = string
}

variable "key_pair_name" {
  description = "Name of the SSH key pair."
  type        = string
}

variable "public_key_path" {
  description = "Path to the public key file."
  type        = string
}

variable "github_token" {
  description = "GitHub Token"
  type        = string
}

variable "github_association" {
  description = "GitHub Association"
  type        = string
}

variable "github_repo" {
  description = "GitHub Repository"
  type        = string
}