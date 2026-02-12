resource "aws_s3_bucket" "b" {
  bucket = "prod-env-murali526-s3-bucket"
  #force_destroy = true

  tags = {
    Name        = "prod-env-murali526-s3-bucket"
    Environment = "Production"
  }
}