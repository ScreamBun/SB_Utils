"""
OSQuery userassist ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Userassist(BaseModel):
    """
    UserAssist Registry Key tracks when a user executes an application from Windows Explorer.
    Examples:
        select * from userassist;
    """
    # Application file path.
    path = TextField()
    # Most recent time application was executed.
    last_execution_time = BigIntegerField()
    # Number of times the application has been executed.
    count = IntegerField()
    # User SID.
    sid = TextField()

    class Meta:
        table_name = "userassist"
