"""
OSQuery block_devices ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class BlockDevices(BaseModel):
    """
    Block (buffered access) device file nodes: disks, ramdisks, and DMG containers.
    """
    # Block device name
    name = TextField()
    # Block device parent name
    parent = TextField()
    # Block device vendor string
    vendor = TextField()
    # Block device model string identifier
    model = TextField()
    # Block device size in blocks
    size = BigIntegerField()
    # Block size in bytes
    block_size = IntegerField()
    # Block device Universally Unique Identifier
    uuid = TextField()
    # Block device type string
    type = TextField()
    # Block device label string
    label = TextField()

    class Meta:
        table_name = "block_devices"
