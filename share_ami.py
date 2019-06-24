import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

latest_ami_id = sorted(ec2_client.describe_images(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                    'AnalysisServer-*',
            ]
        }
    ],
)['Images'], key=itemgetter('CreationDate'))[-1]['ImageId']

latest_image = ec2_resource.Image(latest_ami_id)
latest_image.modify_attribute(
    LaunchPermission={
        'Add': [
            {
                'UserId': '842337631775'
            },
            {
                'UserId': '281782457076'
            },
        ],

    }
)
