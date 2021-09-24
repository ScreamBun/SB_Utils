"""
OSQuery launchd_overrides ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class LaunchdOverrides(BaseModel):
    """
    Override keys, per user, for LaunchDaemons and Agents.
    """
    # Daemon or agent service name
    label = TextField()
    # Name of the override key
    key = TextField()
    # Overridden value
    value = TextField()
    # User ID applied to the override, 0 applies to all
    uid = BigIntegerField()
    # Path to daemon or agent plist
    path = TextField()

    class Meta:
        table_name = "launchd_overrides"
