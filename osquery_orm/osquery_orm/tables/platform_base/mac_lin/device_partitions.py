"""
OSQuery device_partitions ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class DevicePartitions(BaseModel):
    """
    Use TSK to enumerate details about partitions on a disk device.
    """
    # Absolute file path to device node
    device = TextField()  # {'required': True}
    # A partition number or description
    partition = IntegerField()
    # 
    label = TextField()
    # 
    type = TextField()
    # 
    offset = BigIntegerField()
    # Byte size of each block
    blocks_size = BigIntegerField()
    # Number of blocks
    blocks = BigIntegerField()
    # Number of meta nodes
    inodes = BigIntegerField()
    # 
    flags = IntegerField()

    class Meta:
        table_name = "device_partitions"
