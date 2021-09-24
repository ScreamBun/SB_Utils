"""
OSQuery event_taps ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class EventTaps(BaseModel):
    """
    Returns information about installed event taps.
    """
    # Is the Event Tap enabled
    enabled = IntegerField()
    # Unique ID for the Tap
    event_tap_id = IntegerField()
    # The mask that identifies the set of events to be observed.
    event_tapped = TextField()
    # The process ID of the target application
    process_being_tapped = IntegerField()
    # The process ID of the application that created the event tap.
    tapping_process = IntegerField()

    class Meta:
        table_name = "event_taps"
