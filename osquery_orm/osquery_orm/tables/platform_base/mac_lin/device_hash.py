"""
OSQuery device_hash ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class DeviceHash(BaseModel):
    """
    Similar to the hash table, but use TSK and allow block address access.
    """
    # Absolute file path to device node
    device = TextField()  # {'required': True}
    # A partition number
    partition = TextField()  # {'required': True}
    # Filesystem inode number
    inode = BigIntegerField()  # {'required': True}
    # MD5 hash of provided inode data
    md5 = TextField()
    # SHA1 hash of provided inode data
    sha1 = TextField()
    # SHA256 hash of provided inode data
    sha256 = TextField()

    class Meta:
        table_name = "device_hash"
