resource "aws_vpc" "main" {
  cidr_block       = var.vpc_cidr_blcok
  instance_tenancy = var.instance_tenancy

  tags = {
    Name = var.vpc_name
  }
}