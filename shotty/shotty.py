import boto3
import click

session = boto3.Session(profile_name='snapshot')
ec2 = session.resource('ec2')

def list_instances():
    "list EC2 Instancs"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
    return

if __name__ == '__main__':
    list_instances()
    


