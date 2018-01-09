#!/usr/bin/env python

# Let's! 

import boto3

ec2 = boto3.client('ec2')


# [aws_sdk.txt] 4.2.1 Test by describe_instances 
#response = ec2.describe_instances()
#print(response)


response = ec2.authorize_security_group_ingress(
    #CidrIp='84.238.165.180/32', #This is a (university) library. 
    #FromPort=80,
    GroupId='sg-f69bbb9c',
    GroupName='nova-security-grupa-1',
    IpPermissions=[
        {
            'FromPort': 80,
            'IpProtocol': 'TCP',
            'IpRanges': [
                {
                    'CidrIp': '84.238.165.180/32',
                    'Description': 'A university library.'
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