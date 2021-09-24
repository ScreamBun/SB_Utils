"""
OSQuery selinux_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class SelinuxEvents(BaseModel):
    """
    Track SELinux events.
    """
    # Event type
    type = TextField()
    # Message
    message = TextField()
    # Time of execution in UNIX time
    time = BigIntegerField()
    # Time of execution in system uptime
    uptime = BigIntegerField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "selinux_events"
