"""
OSQuery nvram ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Nvram(BaseModel):
    """
    Apple NVRAM variable listing.
    """
    # Variable name
    name = TextField()  # {'additional': True, 'index': True}
    # Data type (CFData, CFString, etc)
    type = TextField()
    # Raw variable data
    value = TextField()

    class Meta:
        table_name = "nvram"
