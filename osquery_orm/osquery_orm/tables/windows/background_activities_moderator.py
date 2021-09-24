"""
OSQuery background_activities_moderator ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class BackgroundActivitiesModerator(BaseModel):
    """
    Background Activities Moderator (BAM) tracks application execution.
    Examples:
        select * from background_activities_moderator;
    """
    # Application file path.
    path = TextField()
    # Most recent time application was executed.
    last_execution_time = BigIntegerField()
    # User SID.
    sid = TextField()

    class Meta:
        table_name = "background_activities_moderator"
