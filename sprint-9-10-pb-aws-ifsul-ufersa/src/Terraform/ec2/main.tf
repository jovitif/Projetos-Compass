resource "aws_key_pair" "deployer" {
  key_name   = var.key_pair_name
  public_key = file(var.public_key_path)
}

resource "aws_instance" "web" {
  ami                    = "ami-0d94353f7bad10668" # Amazon Linux 2 AMI (HVM)
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.deployer.key_name
  subnet_id              = var.subnet_id
  vpc_security_group_ids = [var.security_group_id]
  associate_public_ip_address = true

  user_data = templatefile("${path.module}/user_data.sh", {
    github_token       = var.github_token
    github_association = var.github_association
    github_repo        = var.github_repo
  })

  tags = {
    Project    = ""
    CostCenter = ""
    Name       = "web-server"
  }

  volume_tags = {
    Project    = ""
    CostCenter = ""
    Name       = "web-server-volume"
  }
}

resource "aws_eip" "web_eip" {
  domain = "vpc"

  tags = {
    Name = "web-server-eip"
  }
}

resource "aws_eip_association" "web_eip_assoc" {
  instance_id   = aws_instance.web.id
  allocation_id = aws_eip.web_eip.id
}