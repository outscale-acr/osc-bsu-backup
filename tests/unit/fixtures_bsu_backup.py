instances = {
    "Reservations": [
        {
            "Groups": [
                {
                    "GroupName": "priv",
                    "GroupId": "sg-0fea0dac"
                }
            ],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-b0d57010",
                    "InstanceId": "i-e6b7ab04",
                    "InstanceType": "t2.nano",
                    "KernelId": "",
                    "KeyName": "work",
                    "LaunchTime": "2020-04-09T13:28:58.721Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "eu-west-2a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-0-2-10.eu-west-2.compute.internal",
                    "PrivateIpAddress": "10.0.2.10",
                    "ProductCodes": [],
                    "PublicDnsName": "",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "SubnetId": "subnet-4c66da82",
                    "VpcId": "vpc-ad730e33",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "AttachTime": "2020-04-09T13:28:58.721Z",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-a87f91c1"
                            }
                        }
                    ],
                    "ClientToken": "",
                    "EbsOptimized": False,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": "2020-04-09T13:28:58.721Z",
                                "AttachmentId": "eni-attach-1fb7811e",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached"
                            },
                            "Description": "Primary network interface",
                            "Groups": [
                                {
                                    "GroupName": "priv",
                                    "GroupId": "sg-0fea0dac"
                                }
                            ],
                            "MacAddress": "aa:d6:af:71:91:f6",
                            "NetworkInterfaceId": "eni-a8213f11",
                            "OwnerId": "763630846467",
                            "PrivateDnsName": "ip-10-0-2-10.eu-west-2.compute.internal",
                            "PrivateIpAddress": "10.0.2.10",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-10-0-2-10.eu-west-2.compute.internal",
                                    "PrivateIpAddress": "10.0.2.10"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-4c66da82",
                            "VpcId": "vpc-ad730e33"
                        }
                    ],
                    "RootDeviceName": "/dev/sda1",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "priv",
                            "GroupId": "sg-0fea0dac"
                        }
                    ],
                    "SourceDestCheck": True,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "test1"
                        }
                    ],
                    "VirtualizationType": "hvm"
                }
            ],
            "OwnerId": "763630846467",
            "ReservationId": "r-390600af"
        }
    ]
}

volumes = {
    "Volumes": [
        {
            "Attachments": [
                {
                    "AttachTime": "2019-10-08T17:14:52.314Z",
                    "Device": "/dev/sda1",
                    "InstanceId": "i-8c1d8798",
                    "State": "attached",
                    "VolumeId": "vol-a24fffdc",
                    "DeleteOnTermination": False
                }
            ],
            "AvailabilityZone": "eu-west-2a",
            "CreateTime": "2017-08-10T17:34:59.644Z",
            "Size": 10,
            "SnapshotId": "snap-d1c97efa",
            "State": "in-use",
            "VolumeId": "vol-a24fffdc",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "test1"
                },
                {
                    "Key": "project",
                    "Value": "test2"
                }
            ],

            "VolumeType": "standard"
        }
    ]
}

snapshots1 = {
    "Snapshots": [
        {
            "Description": "osc-bsu-backup 0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-cf4748a5",
            "StartTime": "2019-12-19T16:02:22.204Z",
            "State": "completed",
            "VolumeId": "vol-59b94d63",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-04fd92f4",
            "StartTime": "2019-12-19T16:56:20.567Z",
            "State": "completed",
            "VolumeId": "vol-59b94d63",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-30e1c236",
            "StartTime": "2019-12-19T16:50:09.591Z",
            "State": "completed",
            "VolumeId": "vol-59b94d63",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-d5caf847",
            "StartTime": "2019-12-19T16:53:04.271Z",
            "State": "completed",
            "VolumeId": "vol-59b94d63",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-f820da70",
            "StartTime": "2019-12-19T16:57:03.137Z",
            "State": "completed",
            "VolumeId": "vol-59b94d63",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-e5b47810",
            "StartTime": "2019-12-19T16:57:44.663Z",
            "State": "completed",
            "VolumeId": "vol-59b94d63",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-16959493",
            "StartTime": "2019-12-19T17:21:06.316Z",
            "State": "completed",
            "VolumeId": "vol-59b94d63",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-a8fa23e2",
            "StartTime": "2019-12-19T17:15:09.910Z",
            "State": "completed",
            "VolumeId": "vol-59b94d63",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-14f3772c",
            "StartTime": "2019-12-19T17:18:27.772Z",
            "State": "completed",
            "VolumeId": "vol-59b94d63",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-e9a6aae5",
            "StartTime": "2019-12-19T17:18:54.429Z",
            "State": "completed",
            "VolumeId": "vol-59b94d63",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-70be5243",
            "StartTime": "2019-12-19T17:20:23.850Z",
            "State": "completed",
            "VolumeId": "vol-59b94d63",
            "VolumeSize": 10,
            "Tags": []
        }
    ]
}

snapshots2 = {
    "Snapshots": [
        {
            "Description": "osc-bsu-backup 0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-8f3436c0",
            "StartTime": "2019-12-19T16:02:21.165Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-e6996c10",
            "StartTime": "2019-12-19T16:50:08.496Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-fa25ee50",
            "StartTime": "2019-12-19T16:53:02.217Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-5569bbaa",
            "StartTime": "2019-12-19T17:21:04.153Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-9c3c5d34",
            "StartTime": "2019-12-19T16:56:18.452Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-7729b15f",
            "StartTime": "2019-12-19T16:57:00.779Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-ecead238",
            "StartTime": "2019-12-19T16:57:42.726Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-445be4c7",
            "StartTime": "2019-12-19T17:15:08.852Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-e88add53",
            "StartTime": "2019-12-19T17:18:52.419Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-5e2e73c4",
            "StartTime": "2019-12-19T17:18:26.086Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-11d38c47",
            "StartTime": "2019-12-19T17:19:49.081Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "osc-bsu-backup 0.0.1",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-f3338f81",
            "StartTime": "2019-12-19T17:20:21.762Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        }
    ]
}

create_snapshot1 = {
    "Description": "",
    "Encrypted": False,
    "OwnerId": "763630846467",
    "Progress": "0%",
    "SnapshotId": "snap-91c8d227",
    "StartTime": "2020-04-14T18:32:43.756Z",
    "State": "in-queue",
    "VolumeId": "vol-56d30e10",
    "VolumeSize": 10
}

snapshot_completed1 = {
    "Snapshots": [
        {
            "Description": "",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-91c8d227",
            "StartTime": "2020-04-14T18:32:43.756Z",
            "State": "completed",
            "VolumeId": "vol-56d30e10",
            "VolumeSize": 10,
            "Tags": []
        }
    ]
}

create_snapshot2 = {
    "Description": "",
    "Encrypted": False,
    "OwnerId": "763630846467",
    "Progress": "0%",
    "SnapshotId": "snap-f3338f81",
    "StartTime": "2020-04-14T18:32:43.756Z",
    "State": "in-queue",
    "VolumeId": "vol-640141cf",
    "VolumeSize": 10
}

snapshot_completed2 = {
    "Snapshots": [
        {
            "Description": "",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-f3338f81",
            "StartTime": "2020-04-14T18:32:43.756Z",
            "State": "completed",
            "VolumeId": "vol-640141cf",
            "VolumeSize": 10,
            "Tags": []
        },
        {
            "Description": "",
            "Encrypted": False,
            "OwnerId": "763630846467",
            "Progress": "100%",
            "SnapshotId": "snap-91c8d227",
            "StartTime": "2020-04-14T18:32:43.756Z",
            "State": "completed",
            "VolumeId": "vol-56d30e10",
            "VolumeSize": 10,
            "Tags": []
        }

    ]
}