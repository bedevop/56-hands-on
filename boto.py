import boto3 as B3

aws_access_key_id = ''
aws_secret_access_key = ''

client = B3.client('ec2', region_name='us-east-2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
response = client.describe_instances()
print(response)
