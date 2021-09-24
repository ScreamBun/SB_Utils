"""
OSQuery running_apps ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class RunningApps(BaseModel):
    """
    macOS applications currently running on the host system.
    """
    # The pid of the application
    pid = IntegerField()  # {'index': True}
    # The bundle identifier of the application
    bundle_identifier = TextField()
    # 1 if the application is in focus, 0 otherwise
    is_active = IntegerField()  # {'additional': True}

    class Meta:
        table_name = "running_apps"
