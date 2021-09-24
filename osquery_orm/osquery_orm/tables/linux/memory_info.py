"""
OSQuery memory_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField


class MemoryInfo(BaseModel):
    """
    Main memory information in bytes.
    """
    # Total amount of physical RAM, in bytes
    memory_total = BigIntegerField()
    # The amount of physical RAM, in bytes, left unused by the system
    memory_free = BigIntegerField()
    # The amount of physical RAM, in bytes, used for file buffers
    buffers = BigIntegerField()
    # The amount of physical RAM, in bytes, used as cache memory
    cached = BigIntegerField()
    # The amount of swap, in bytes, used as cache memory
    swap_cached = BigIntegerField()
    # The total amount of buffer or page cache memory, in bytes, that is in active use
    active = BigIntegerField()
    # The total amount of buffer or page cache memory, in bytes, that are free and available
    inactive = BigIntegerField()
    # The total amount of swap available, in bytes
    swap_total = BigIntegerField()
    # The total amount of swap free, in bytes
    swap_free = BigIntegerField()

    class Meta:
        table_name = "memory_info"
