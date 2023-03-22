resource "aws_s3_bucket" "buckets-for-data-lake" {
  for_each          = { for idx, bucket in var.bucket_datalake : idx => bucket }
  bucket            = each.value
  acl = "private"
}

variable "bucket_datalake" {
  type        = list(string)
  description = "name of the buckets for datalake"
  default     = ["wu2landing"]
}

output "bucket_arns" {
  value = tolist([for bucket in aws_s3_bucket.buckets-for-data-lake : bucket.arn])
}



