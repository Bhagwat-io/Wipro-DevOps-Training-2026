# public subnet

resource "aws_subnet" "main-pub-sub" {
  vpc_id     = var.vpc_id
  cidr_block = var.pub_subnet_cidr_block
  availability_zone = var.pub_subnet_az

  tags = {
    Name = var.pub_subnet_name
  }
}