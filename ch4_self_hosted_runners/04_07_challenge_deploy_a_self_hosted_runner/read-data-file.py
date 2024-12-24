import os
import boto3

def get_parameter(parameter_name):
    """Fetches a parameter value from AWS Systems Manager Parameter Store."""
    try:
        ssm_client = boto3.client('ssm', region_name=os.getenv('AWS_REGION', 'us-east-1'))
        response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
        return response['Parameter']['Value']
    except Exception as e:
        print(f"Error fetching parameter {parameter_name}: {e}")
        raise

def read_file(file_path):
    """Reads the contents of a file given its file path."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        raise

if __name__ == "__main__":
    PARAMETER_NAME = "DATA_FILE"

    print("Fetching parameter from Parameter Store...")
    file_path = get_parameter(PARAMETER_NAME)

    print(f"Parameter value: {file_path}")

    print("Reading file contents...")
    file_contents = read_file(file_path)

    print("File Contents:")
    print(file_contents)
