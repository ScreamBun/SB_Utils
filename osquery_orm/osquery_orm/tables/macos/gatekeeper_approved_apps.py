"""
OSQuery gatekeeper_approved_apps ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField, DoubleField


class GatekeeperApprovedApps(BaseModel):
    """
    Gatekeeper apps a user has allowed to run.
    """
    path = TextField(help_text="Path of executable allowed to run")
    requirement = TextField(help_text="Code signing requirement language")
    ctime = DoubleField(help_text="Last change time")
    mtime = DoubleField(help_text="Last modification time")

    class Meta:
        table_name = "gatekeeper_approved_apps"
