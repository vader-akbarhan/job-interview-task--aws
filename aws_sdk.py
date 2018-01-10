#!/usr/bin/env python

# Let's! 

import boto3
import sys
from os import system

ec2 = boto3.client('ec2')
s3 = boto3.resource("s3")


# [aws_sdk.txt] 4.2.1 Test by describe_instances 
#response = ec2.describe_instances()
#print(response)

def allow_http():
    my_ip = str(raw_input("Please enter your IP so that I would allow you to HTTP: "))
    response = ec2.authorize_security_group_ingress(
        #CidrIp='string',  
        #FromPort=80,
        GroupId='sg-f69bbb9c',
        GroupName='nova-security-grupa-1',
        IpPermissions=[
            {
                'FromPort': 80,
                'IpProtocol': 'TCP',
                'IpRanges': [
                    {
                        'CidrIp': my_ip,
                        'Description': 'A new place - test 2.'
                    },
                ],
            #    'Ipv6Ranges': [
            #        {
            #            'CidrIpv6': 'string',
            #            'Description': 'string'
            #        },
            #    ],
            #    'PrefixListIds': [
            #        {
            #            'Description': 'string',
            #            'PrefixListId': 'string'
            #        },
            #    ],
                'ToPort': 80,
            #    'UserIdGroupPairs': [
            #        {
            #            'Description': 'string',
            #            'GroupId': 'string',
            #            'GroupName': 'string',
            #            'PeeringStatus': 'string',
            #            'UserId': 'string',
            #            'VpcId': 'string',
            #            'VpcPeeringConnectionId': 'string'
            #        },
            #    ]
            },
        ],
        #IpProtocol='TCP', # [aws_sdk.txt 5.] "ipProtocol" is "(VPC only)". 
        #SourceSecurityGroupName='string',
        #SourceSecurityGroupOwnerId='string',
        #ToPort=80,
        DryRun=False
)

def create_bucket():
    kofa = str(raw_input("Enter a name for a new bucket: "))
    try:
        response = s3.create_bucket(Bucket=(kofa), CreateBucketConfiguration={
        'LocationConstraint': 'eu-central-1'})
        print response
    except Exception as error:
        print error

if __name__ == "__main__":
    allow_http() 
    create_bucket()