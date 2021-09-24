"""
OSQuery suid_bin ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class SuidBin(BaseModel):
    """
    suid binaries in common locations.
    """
    # Binary path
    path = TextField()
    # Binary owner username
    username = TextField()
    # Binary owner group
    groupname = TextField()
    # Binary permissions
    permissions = TextField()

    class Meta:
        table_name = "suid_bin"
