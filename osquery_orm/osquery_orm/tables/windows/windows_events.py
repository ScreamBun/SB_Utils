"""
OSQuery windows_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class WindowsEvents(BaseModel):
    """
    Windows Event logs.
    Examples:
        select * from windows_events where eventid=4104 and source='Security'
    """
    # Timestamp the event was received
    time = BigIntegerField()
    # System time at which the event occurred
    datetime = TextField()
    # Source or channel of the event
    source = TextField()
    # Provider name of the event
    provider_name = TextField()
    # Provider guid of the event
    provider_guid = TextField()
    # Hostname of system where event was generated
    computer_name = TextField()
    # Event ID of the event
    eventid = IntegerField()
    # Task value associated with the event
    task = IntegerField()
    # The severity level associated with the event
    level = IntegerField()
    # A bitmask of the keywords defined in the event
    keywords = TextField()
    # Data associated with the event
    data = TextField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "windows_events"
