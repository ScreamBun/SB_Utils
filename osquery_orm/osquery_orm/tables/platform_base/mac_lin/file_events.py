"""
OSQuery file_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class FileEvents(BaseModel):
    """
    Track time/action changes to files specified in configuration data.
    """
    # The path associated with the event
    target_path = TextField()
    # The category of the file defined in the config
    category = TextField()
    # Change action (UPDATE, REMOVE, etc)
    action = TextField()
    # ID used during bulk update
    transaction_id = BigIntegerField()
    # Filesystem inode number
    inode = BigIntegerField()
    # Owning user ID
    uid = BigIntegerField()
    # Owning group ID
    gid = BigIntegerField()
    # Permission bits
    mode = TextField()
    # Size of file in bytes
    size = BigIntegerField()
    # Last access time
    atime = BigIntegerField()
    # Last modification time
    mtime = BigIntegerField()
    # Last status change time
    ctime = BigIntegerField()
    # The MD5 of the file after change
    md5 = TextField()
    # The SHA1 of the file after change
    sha1 = TextField()
    # The SHA256 of the file after change
    sha256 = TextField()
    # 1 if the file was hashed, 0 if not, -1 if hashing failed
    hashed = IntegerField()
    # Time of file event
    time = BigIntegerField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "file_events"
