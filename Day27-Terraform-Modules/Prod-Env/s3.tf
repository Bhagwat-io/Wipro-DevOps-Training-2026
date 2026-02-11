resource "aws_s3_bucket" "b" {
  bucket = "prod-env-murali526-s3-bucket"

  tags = {
    Name        = "prod-env-murali526-s3-bucket"
    Environment = "Production"
  }
}