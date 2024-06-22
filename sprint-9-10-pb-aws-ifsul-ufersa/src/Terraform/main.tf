provider "aws" {
  region = var.aws_region
}

module "vpc" {
  source = "./vpc"
  vpc_cidr = var.vpc_cidr
}

module "security_group" {
  source    = "./security_group"
  vpc_id    = module.vpc.vpc_id
}

module "ec2" {
  source              = "./ec2"
  subnet_id           = module.vpc.subnet_id
  security_group_id   = module.security_group.security_group_id
  key_pair_name       = var.key_pair_name
  public_key_path     = var.public_key_path
  github_association  = var.github_association
  github_repo         = var.github_repo
  github_token        = var.github_token
}
