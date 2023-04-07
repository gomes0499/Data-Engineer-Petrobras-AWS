# Configure the backend to store state in S3
terraform {
  backend "s3" {
    bucket = "2-project-data-engineer-tf-state"
    key = "2-project-data-engineer-tf-state"
    region = "us-east-1"
  }
}