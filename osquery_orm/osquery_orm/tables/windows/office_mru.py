"""
OSQuery office_mru ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class OfficeMru(BaseModel):
    """
    View recently opened Office documents.
    Examples:
        select * from office_mru;
    """
    # Associated Office application
    application = TextField()
    # Office application version number
    version = TextField()
    # File path
    path = TextField()
    # Most recent opened time file was opened
    last_opened_time = BigIntegerField()
    # User SID
    sid = TextField()

    class Meta:
        table_name = "office_mru"
