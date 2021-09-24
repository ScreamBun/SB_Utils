"""
OSQuery gatekeeper_approved_apps ORM
"""
from osquery_orm.orm import BaseModel
from peewee import DoubleField, TextField


class GatekeeperApprovedApps(BaseModel):
    """
    Gatekeeper apps a user has allowed to run.
    """
    # Path of executable allowed to run
    path = TextField()
    # Code signing requirement language
    requirement = TextField()
    # Last change time
    ctime = DoubleField()
    # Last modification time
    mtime = DoubleField()

    class Meta:
        table_name = "gatekeeper_approved_apps"
