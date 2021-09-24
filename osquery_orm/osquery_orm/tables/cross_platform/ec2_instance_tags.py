"""
OSQuery ec2_instance_tags ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Ec2InstanceTags(BaseModel):
    """
    EC2 instance tag key value pairs.
    Examples:
        select * from ec2_instance_tags
    """
    # EC2 instance ID
    instance_id = TextField()
    # Tag key
    key = TextField()
    # Tag value
    value = TextField()

    class Meta:
        table_name = "ec2_instance_tags"
