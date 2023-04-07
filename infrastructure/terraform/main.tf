# Call the Kinesis Module
module "Kinesis" {
source = "./modules/kinesis"
bucket_arns = module.S3.bucket_arns
}

# Call the S3 Module
module "S3" {
  source = "./modules/s3"
}


