"""
OSQuery shared_memory ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class SharedMemory(BaseModel):
    """
    OS shared memory regions.
    """
    # Shared memory segment ID
    shmid = IntegerField()
    # User ID of owning process
    owner_uid = BigIntegerField()
    # User ID of creator process
    creator_uid = BigIntegerField()
    # Process ID to last use the segment
    pid = BigIntegerField()
    # Process ID that created the segment
    creator_pid = BigIntegerField()
    # Attached time
    atime = BigIntegerField()
    # Detached time
    dtime = BigIntegerField()
    # Changed time
    ctime = BigIntegerField()
    # Memory segment permissions
    permissions = TextField()
    # Size in bytes
    size = BigIntegerField()
    # Number of attached processes
    attached = IntegerField()
    # Destination/attach status
    status = TextField()
    # 1 if segment is locked else 0
    locked = IntegerField()

    class Meta:
        table_name = "shared_memory"
