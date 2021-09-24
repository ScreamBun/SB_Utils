"""
OSQuery xprotect_reports ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class XprotectReports(BaseModel):
    """
    Database of XProtect matches (if user generated/sent an XProtect report).
    """
    # Description of XProtected malware
    name = TextField()
    # Action taken by user after prompted
    user_action = TextField()
    # Quarantine alert time
    time = TextField()

    class Meta:
        table_name = "xprotect_reports"
