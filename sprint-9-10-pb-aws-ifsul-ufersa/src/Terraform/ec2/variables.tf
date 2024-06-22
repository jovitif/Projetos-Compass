variable "subnet_id" {
  description = "The ID of the subnet."
}

variable "security_group_id" {
  description = "The ID of the security group."
}

variable "key_pair_name" {
  description = "The name of the SSH key pair."
}

variable "public_key_path" {
  description = "The path to the public key file."
}

variable "github_token" {
  description = "GitHub Token"
}

variable "github_association" {
  description = "GitHub Association"
}

variable "github_repo" {
  description = "GitHub Repository"
}
