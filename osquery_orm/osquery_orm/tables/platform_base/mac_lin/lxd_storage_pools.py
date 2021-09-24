"""
OSQuery lxd_storage_pools ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class LxdStoragePools(BaseModel):
    """
    LXD storage pool information.
    Examples:
        select * from lxd_storage_pools
    """
    # Name of the storage pool
    name = TextField()
    # Storage driver
    driver = TextField()
    # Storage pool source
    source = TextField()
    # Size of the storage pool
    size = TextField()
    # Storage space used in bytes
    space_used = BigIntegerField()
    # Total available storage space in bytes for this storage pool
    space_total = BigIntegerField()
    # Number of inodes used
    inodes_used = BigIntegerField()
    # Total number of inodes available in this storage pool
    inodes_total = BigIntegerField()

    class Meta:
        table_name = "lxd_storage_pools"
