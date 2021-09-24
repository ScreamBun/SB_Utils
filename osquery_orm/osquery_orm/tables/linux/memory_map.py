"""
OSQuery memory_map ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class MemoryMap(BaseModel):
    """
    OS memory region map.
    """
    # Region name
    name = TextField()
    # Start address of memory region
    start = TextField()
    # End address of memory region
    end = TextField()

    class Meta:
        table_name = "memory_map"
