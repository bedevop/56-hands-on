import boto3 as B3

aws_access_key_id = 'AKIARGGLAIJJFVZ3D45C'
aws_secret_access_key = '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'

client = B3.client('ec2', region_name='us-east-2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
response = client.describe_instances()
print(response)