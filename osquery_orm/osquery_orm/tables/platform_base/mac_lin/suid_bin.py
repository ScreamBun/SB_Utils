"""
OSQuery suid_bin ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class SuidBin(BaseModel):
    """
    suid binaries in common locations.
    """
    path = TextField(help_text="Binary path")
    username = TextField(help_text="Binary owner username")
    groupname = TextField(help_text="Binary owner group")
    permissions = TextField(help_text="Binary permissions")

    class Meta:
        table_name = "suid_bin"
