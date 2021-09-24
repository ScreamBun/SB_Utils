"""
OSQuery logged_in_users ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class LoggedInUsers(BaseModel):
    """
    Users with an active shell on the system.
    """
    # Login type
    type = TextField()
    # User login name
    user = TextField()
    # Device name
    tty = TextField()
    # Remote hostname
    host = TextField()
    # Time entry was made
    time = BigIntegerField()
    # Process (or thread) ID
    pid = IntegerField()

    class Meta:
        table_name = "logged_in_users"


# OS specific properties for Windows
class Windows_LoggedInUsers(LoggedInUsers):
    # The user's unique security identifier
    sid = TextField()
    # HKEY_USERS registry hive
    registry_hive = TextField()
