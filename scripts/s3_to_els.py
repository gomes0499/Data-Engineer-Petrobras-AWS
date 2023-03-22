import boto3
import json
from elasticsearch import Elasticsearch, helpers
import configparser

config = configparser.ConfigParser()
config.read("/Users/gomes/Desktop/Projects/Data Engineer/2-Project/config/config.ini")

bucket_name = config.get("s3", "bucket_landing")
elasticsearch_index = config.get("elasticsearch", "index")

def read_from_s3_and_write_to_elasticsearch(bucket_name, elasticsearch_index):
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # List all objects in the bucket
    objects = s3_client.list_objects_v2(Bucket=bucket_name)

    # Read data from each object in the bucket
    records = []
    for obj in objects["Contents"]:
        key = obj["Key"]
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        file_content = response["Body"].read().decode('utf-8')
        for line in file_content.splitlines():
            # Convert each line to a Python dictionary
            record = json.loads(line)
            records.append(record)

    # Initialize the Elasticsearch client
    es = Elasticsearch("http://localhost:9200")  # Replace with your Elasticsearch instance URL

    # Prepare the data for Elasticsearch
    actions = []
    for record in records:
        action = {
            '_op_type': 'index',
            '_index': elasticsearch_index,
            '_source': record
        }
        actions.append(action)

    # Write the data to Elasticsearch
    helpers.bulk(es, actions)

# Example usage:
read_from_s3_and_write_to_elasticsearch(bucket_name, elasticsearch_index)
