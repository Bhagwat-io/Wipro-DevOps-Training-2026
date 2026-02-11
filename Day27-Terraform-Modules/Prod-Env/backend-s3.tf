terraform {
  backend "s3" {
    bucket = "prod-env-murali526-s3-bucket"
    key    = "prod/terraform.tfstate"
    region = "us-east-2"
  }
}