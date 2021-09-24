"""
OSQuery azure_instance_tags ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class AzureInstanceTags(BaseModel):
    """
    Azure instance tags.
    Examples:
        select * from ec2_instance_tags
    """
    # Unique identifier for the VM
    vm_id = TextField()
    # The tag key
    key = TextField()
    # The tag value
    value = TextField()

    class Meta:
        table_name = "azure_instance_tags"
