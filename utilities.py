import boto3

ssm = boto3.client('ssm')


def get_parameter(parameter_name):
    response = ssm.get_parameter(Name=f"/{parameter_name}", WithDecryption=True)
    return response['Parameter']['Value']
