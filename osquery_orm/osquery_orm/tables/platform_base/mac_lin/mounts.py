"""
OSQuery mounts ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class Mounts(BaseModel):
    """
    System mounted devices and filesystems (not process specific).
    """
    # Mounted device
    device = TextField()
    # Mounted device alias
    device_alias = TextField()
    # Mounted device path
    path = TextField()
    # Mounted device type
    type = TextField()
    # Block size in bytes
    blocks_size = BigIntegerField()
    # Mounted device used blocks
    blocks = BigIntegerField()
    # Mounted device free blocks
    blocks_free = BigIntegerField()
    # Mounted device available blocks
    blocks_available = BigIntegerField()
    # Mounted device used inodes
    inodes = BigIntegerField()
    # Mounted device free inodes
    inodes_free = BigIntegerField()
    # Mounted device flags
    flags = TextField()

    class Meta:
        table_name = "mounts"
