import boto3
ec2 = boto3.client('ec2')
## This function will return list of instance ids which are schedules
def get_scheduled_instances():
    instance_ids = []
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:schedule',
                'Values': [
                    'true',
                ]
            },
        ]
    )
    metadata_ec2 = response['Reservations']
    for data in metadata_ec2:
        for instance in data['Instances']:
            instance_ids.append(instance['InstanceId'])
    return instance_ids
def stop_scheduled_instances(instance_ids):
    for instance_id in instance_ids:
        ec2_instance_status = ''
        response = ec2.describe_instances(InstanceIds=[instance_id])
        ec2_instance_status= response['Reservations'][0]['Instances'][0]['State']['Name']
        
        if (ec2_instance_status == 'stopped'):
            print(f"{instance_id} is already in stopped state")
        elif(ec2_instance_status == 'running'):
            print(f"{instance_id} will be stopped")
            ec2.stop_instances(InstanceIds=[instance_id])
        else:
            print("{instance_id} status is unknown at the moment, please try again after sometime")
def start_scheduled_instances(instance_ids):
    for instance_id in instance_ids:
        ec2_instance_status = ''
        response = ec2.describe_instances(InstanceIds=[instance_id])
        ec2_instance_status= response['Reservations'][0]['Instances'][0]['State']['Name']
        
        if (ec2_instance_status == 'running'):
            print(f"{instance_id} is already in running state")
        elif(ec2_instance_status == 'stopped'):
            print(f"{instance_id} will be started")
            ec2.start_instances(InstanceIds=[instance_id])
        else:
            print("{instance_id} status is unknown at the moment, please try again after sometime")

instance_ids = get_scheduled_instances()
# stop_scheduled_instances(instance_ids)
start_scheduled_instances(instance_ids)






