output "web_eip" {
  value = module.ec2.web_eip.public_ip
}

output "security_group_id" {
  value = module.security_group.security_group_id
}

output "subnet_id" {
  value = module.vpc.subnet_id
}

output "vpc_id" {
  value = module.vpc.vpc_id
}

output "github_token" {
  value = var.github_token
}

output "github_association" {
  value = var.github_association
}

output "github_repo" {
  value = var.github_repo
}