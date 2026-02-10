resource "aws_vpc" "main" {
  cidr_block       = var.vpc_cidr_blcok
  instance_tenancy = var.instance_tenancy

  tags = {
    Name = var.vpc_name
  }
}

# public subnet

resource "aws_subnet" "main-pub-sub" {
  vpc_id     = aws_vpc.main.id
  cidr_block = var.pub_subnet_cidr_block
  availability_zone = var.pub_subnet_az

  tags = {
    Name = var.pub_subnet_name
  }
}

# private subnet

resource "aws_subnet" "main-prvt-sub" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "murali-prvt-subnet"
  }
}

# internet gateway

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "murali-igw-new"
  }
}

# public route table

resource "aws_route_table" "pub-rt" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"   # destination address
    gateway_id = aws_internet_gateway.gw.id   # target address
  }

  tags = {
    Name = "murali-pub-rt"
  }
}

# associate public subnet with public route table

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.main-pub-sub.id
  route_table_id = aws_route_table.pub-rt.id
}

# elastic ip address

resource "aws_eip" "lb" {

   tags = {
    Name = "murali-eip"
    }
}

# nat gateway 

resource "aws_nat_gateway" "example" {
  allocation_id = aws_eip.lb.id
  subnet_id     = aws_subnet.main-pub-sub.id

  tags = {
    Name = "murali-gw-NAT"
  }

}

# private route table

resource "aws_route_table" "prvt-rt" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"   # destination address
    gateway_id = aws_nat_gateway.example.id   # target address
  }

  tags = {
    Name = "murali-prvt-rt"
  }
}

# associate private subnet with private route table

resource "aws_route_table_association" "b" {
  subnet_id      = aws_subnet.main-prvt-sub.id
  route_table_id = aws_route_table.prvt-rt.id
}

# create key pair

resource "aws_key_pair" "deployer" {
  key_name   = "murali-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDgshOigNlnR6HOE+z0MKf6LRtHRqi97PjodeyY2ZERTN5GJvWVoB2l6pvRIgCJkkdnfd6Cjqg/EVsfVbzwmr1hO5YiD+obgsF0Pniv2s6hF0LzlEBBq/uj57lZDcTbkqMyEZSSVQ62+wVJgeEaqt/f6/Q5dmljYOknqp9TX+WOjWD5qTaXqzjYyiQWG1344WYkaXwIf+5ubdKCR0lcosqxir+vfHVohnoiDdjzfc/txmjXnk357rt6f0bXL2avLxPdToVhBtuS6IUuXtu9Bw71rWXd7puhwYWs/EulH7CG57bWPXNl8HKr9A/q+wgbb/2nAQqWD0ko2yh61VYTyiFq1tQgWa1qdWPqnG1NEtDSKz8hqMuWQasvrT5vTzrs95eq5QkZdeKSftl1XtsqXTkyy1OVL9jbcWX/9ML6k2M7WOc0KMBudBu9oDZTHVUEMCI8dqoc0GmiCGxn47pVTSy4faq6x7mOtxzNXtSlQlzwshGUD+SL02sabe+GkCxwb4ZMO+qbOpmpdGXWNYiTAhyfgNMMDpHS7Tv/e/hlKG/5XTE2/SFVqgNaMJdLg+gs6rUIEYXJVOorE88e254Je2YYRn4Av/4J34M8YwzFMTaoYDuRhxQ+/6B9l+DAKyjKp1ymH3XxzHQ7I/DpCWYjB2bDLEO0Vj0stNIffMkXdep21Q== david prabhakar y@KING-DAVID"
}

# create security group

resource "aws_security_group" "murali-sg" {
  name        = "murali-sg"
  description = "Allow TLS inbound traffic and all outbound traffic"
  vpc_id      = aws_vpc.main.id

  tags = {
    Name = "murali-sg"
  }

    ingress {
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
    
    ingress {
    from_port        = 8080
    to_port          = 8080
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

    ingress {
    from_port        = 9000
    to_port          = 9000
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
    egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }
}

# create ec2 instance in public subnet 


resource "aws_instance" "public-instance" {
  ami           = "ami-0b6c6ebed2801a5cb"
  instance_type = "t2.micro"
  key_name = "murali-key"
  count = 1
  vpc_security_group_ids = [aws_security_group.murali-sg.id]
  subnet_id = aws_subnet.main-pub-sub.id
  associate_public_ip_address = true


  tags = {
    Name = "murali-public-instance"
  }
}

# create ec2 instance in private subnet
resource "aws_instance" "private-instance" {
  ami           = "ami-0b6c6ebed2801a5cb"
  instance_type = "t2.micro"
  key_name = "murali-key"
  vpc_security_group_ids = [ aws_security_group.murali-sg.id ]
  subnet_id = aws_subnet.main-prvt-sub.id
  associate_public_ip_address = false


  tags = {
    Name = "murali-private-instance"
  }
}

