"""
OSQuery syslog_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class SyslogEvents(BaseModel):
    """
    
    """
    # Current unix epoch time
    time = BigIntegerField()
    # Time known to syslog
    datetime = TextField()
    # Hostname configured for syslog
    host = TextField()
    # Syslog severity
    severity = IntegerField()
    # Syslog facility
    facility = TextField()
    # The syslog tag
    tag = TextField()
    # The syslog message
    message = TextField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "syslog_events"
