"""
OSQuery windows_eventlog ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class WindowsEventlog(BaseModel):
    """
    Table for querying all recorded Windows event logs.
    Examples:
        select * from windows_eventlog where eventid=4625 and channel='Security'
    """
    # Source or channel of the event
    channel = TextField()  # {'required': True}
    # System time at which the event occurred
    datetime = TextField()
    # Task value associated with the event
    task = IntegerField()
    # Severity level associated with the event
    level = IntegerField()
    # Provider name of the event
    provider_name = TextField()
    # Provider guid of the event
    provider_guid = TextField()
    # Hostname of system where event was generated
    computer_name = TextField()
    # Event ID of the event
    eventid = IntegerField()  # {'additional': True}
    # A bitmask of the keywords defined in the event
    keywords = TextField()
    # Data associated with the event
    data = TextField()
    # Process ID which emitted the event record
    pid = IntegerField()  # {'additional': True}
    # Thread ID which emitted the event record
    tid = IntegerField()
    # System time to selectively filter the events
    time_range = TextField()  # {'hidden': True, 'additional': True}
    # Timestamp to selectively filter the events
    timestamp = TextField()  # {'hidden': True, 'additional': True}
    # The custom query to filter events
    xpath = TextField()  # {'hidden': True, 'required': True}

    class Meta:
        table_name = "windows_eventlog"
