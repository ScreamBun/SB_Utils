"""
OSQuery user_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class UserEvents(BaseModel):
    """
    Track user events from the audit framework.
    """
    # User ID
    uid = BigIntegerField()
    # Audit User ID
    auid = BigIntegerField()
    # Process (or thread) ID
    pid = BigIntegerField()
    # Message from the event
    message = TextField()
    # The file description for the process socket
    type = IntegerField()
    # Supplied path from event
    path = TextField()
    # The Internet protocol address or family ID
    address = TextField()
    # The network protocol ID
    terminal = TextField()
    # Time of execution in UNIX time
    time = BigIntegerField()
    # Time of execution in system uptime
    uptime = BigIntegerField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "user_events"
