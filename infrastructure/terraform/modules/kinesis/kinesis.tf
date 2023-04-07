resource "aws_kinesis_stream" "test_stream" {
  name             = "wu2-kinesis-stream"
  shard_count      = 1
  retention_period = 48

  shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
  ]

  stream_mode_details {
    stream_mode = "PROVISIONED"
  }

  tags = {
    Environment = "test"
  }
}

# resource "aws_kinesis_firehose_delivery_stream" "s3_stream" {
#   name        = "wu2-kinesis-firehose-s3-stream"
#   destination = "s3"

#   s3_configuration {
#     role_arn   = aws_iam_role.firehose_role.arn
#     bucket_arn = element(module.s3.bucket_arns, 0)
#   }
  
# }

data "aws_iam_policy_document" "firehose_assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["firehose.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "firehose_role" {
  name               = "firehose_test_role"
  assume_role_policy = data.aws_iam_policy_document.firehose_assume_role.json
}

module "s3" {
    source = "../s3/"
}

variable "bucket_arns" {
  description = "List of S3 bucket ARNs"
  type        = list(string)
}
