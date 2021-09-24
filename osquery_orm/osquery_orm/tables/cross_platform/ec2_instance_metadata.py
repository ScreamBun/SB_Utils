"""
OSQuery ec2_instance_metadata ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Ec2InstanceMetadata(BaseModel):
    """
    EC2 instance metadata.
    Examples:
        select * from ec2_instance_metadata
    """
    # EC2 instance ID
    instance_id = TextField()
    # EC2 instance type
    instance_type = TextField()
    # Hardware architecture of this EC2 instance
    architecture = TextField()
    # AWS region in which this instance launched
    region = TextField()
    # Availability zone in which this instance launched
    availability_zone = TextField()
    # Private IPv4 DNS hostname of the first interface of this instance
    local_hostname = TextField()
    # Private IPv4 address of the first interface of this instance
    local_ipv4 = TextField()
    # MAC address for the first network interface of this EC2 instance
    mac = TextField()
    # Comma separated list of security group names
    security_groups = TextField()
    # If there is an IAM role associated with the instance, contains instance profile ARN
    iam_arn = TextField()
    # AMI ID used to launch this EC2 instance
    ami_id = TextField()
    # ID of the reservation
    reservation_id = TextField()
    # AWS account ID which owns this EC2 instance
    account_id = TextField()
    # SSH public key. Only available if supplied at instance launch time
    ssh_public_key = TextField()

    class Meta:
        table_name = "ec2_instance_metadata"
