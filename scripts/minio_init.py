#!/usr/bin/env python3
import os, boto3

S3_ENDPOINT = os.getenv("S3_ENDPOINT", "http://localhost:9000")
ACCESS = os.getenv("S3_ACCESS_KEY", "fixpro")
SECRET = os.getenv("S3_SECRET_KEY", "fixprosecret")
BUCKET = os.getenv("S3_BUCKET", "fixpro-media")
REGION = os.getenv("S3_REGION", "us-east-1")
SECURE = os.getenv("S3_SECURE", "false").lower() == "true"

s3 = boto3.client(
    "s3",
    endpoint_url=S3_ENDPOINT,
    aws_access_key_id=ACCESS,
    aws_secret_access_key=SECRET,
    region_name=REGION,
    use_ssl=SECURE,
)

existing = [b["Name"] for b in s3.list_buckets().get("Buckets", [])]
if BUCKET not in existing:
    s3.create_bucket(Bucket=BUCKET)
    print(f"Bucket '{BUCKET}' creado.")
else:
    print(f"Bucket '{BUCKET}' ya existe.")
