import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    instance_id = 'i-0b5afa23f751d3979'

    try:
        print("Starting EC2 instance termination process")
        response = ec2.describe_instances(
            InstanceIds=[instance_id]
        )
        print("Describe Instances Response:", response)

        instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']
        print("Current Instance State:", instance_state)

        if instance_state == 'running':
            terminate_response = ec2.terminate_instances(
                InstanceIds=[instance_id]
            )
            print("Terminate Instances Response:", terminate_response)
            return {
                'statusCode': 200,
                'body': f"Instance {instance_id} is terminated. Details: {terminate_response}"
            }
        else:
            print(f"Instance {instance_id} is not in a 'running' state.")
            return {
                'statusCode': 200,
                'body': f"Instance {instance_id} is not in 'running' state. Current state: {instance_state}"
            }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error occurred: {str(e)}"
        }
