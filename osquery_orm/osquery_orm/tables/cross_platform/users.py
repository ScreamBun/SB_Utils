"""
OSQuery users ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Users(BaseModel):
    """
    Local user accounts (including domain accounts that have logged on locally (Windows)).
    Examples:
        select * from users where uid = 1000
        select * from users where username = 'root'
        select count(*) from users u, user_groups ug where u.uid = ug.uid
    """
    # User ID
    uid = BigIntegerField()  # {'index': True}
    # Group ID (unsigned)
    gid = BigIntegerField()
    # User ID as int64 signed (Apple)
    uid_signed = BigIntegerField()
    # Default group ID as int64 signed (Apple)
    gid_signed = BigIntegerField()
    # Username
    username = TextField()  # {'additional': True}
    # Optional user description
    description = TextField()
    # User's home directory
    directory = TextField()
    # User's configured default shell
    shell = TextField()
    # User's UUID (Apple) or SID (Windows)
    uuid = TextField()  # {'index': True}

    class Meta:
        table_name = "users"


# OS specific properties for Windows
class Windows_Users(Users):
    # Whether the account is roaming (domain), local, or a system profile
    type = TextField()


# OS specific properties for MacOS
class MacOS_Users(Users):
    # IsHidden attribute set in OpenDirectory
    is_hidden = IntegerField()
