"""
OSQuery device_file ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class DeviceFile(BaseModel):
    """
    Similar to the file table, but use TSK and allow block address access.
    """
    # Absolute file path to device node
    device = TextField()  # {'index': True, 'required': True}
    # A partition number
    partition = TextField()  # {'index': True, 'required': True}
    # A logical path within the device node
    path = TextField()  # {'additional': True}
    # Name portion of file path
    filename = TextField()
    # Filesystem inode number
    inode = BigIntegerField()  # {'index': True}
    # Owning user ID
    uid = BigIntegerField()
    # Owning group ID
    gid = BigIntegerField()
    # Permission bits
    mode = TextField()
    # Size of file in bytes
    size = BigIntegerField()
    # Block size of filesystem
    block_size = IntegerField()
    # Last access time
    atime = BigIntegerField()
    # Last modification time
    mtime = BigIntegerField()
    # Creation time
    ctime = BigIntegerField()
    # Number of hard links
    hard_links = IntegerField()
    # File status
    type = TextField()

    class Meta:
        table_name = "device_file"
