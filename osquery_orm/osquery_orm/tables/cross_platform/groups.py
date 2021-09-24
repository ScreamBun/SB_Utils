"""
OSQuery groups ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Groups(BaseModel):
    """
    Local system groups.
    Examples:
        select * from groups where gid = 0
    """
    # Unsigned int64 group ID
    gid = BigIntegerField()  # {'index': True}
    # A signed int64 version of gid
    gid_signed = BigIntegerField()
    # Canonical local group name
    groupname = TextField()

    class Meta:
        table_name = "groups"


# OS specific properties for Windows
class Windows_Groups(Groups):
    # Unique group ID
    group_sid = TextField()  # {'index': True}
    # Remarks or comments associated with the group
    comment = TextField()


# OS specific properties for MacOS
class MacOS_Groups(Groups):
    # IsHidden attribute set in OpenDirectory
    is_hidden = IntegerField()
