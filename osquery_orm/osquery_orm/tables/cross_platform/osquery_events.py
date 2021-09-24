"""
OSQuery osquery_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class OsqueryEvents(BaseModel):
    """
    Information about the event publishers and subscribers.
    """
    # Event publisher or subscriber name
    name = TextField()
    # Name of the associated publisher
    publisher = TextField()
    # Either publisher or subscriber
    type = TextField()
    # Number of subscriptions the publisher received or subscriber used
    subscriptions = IntegerField()
    # Number of events emitted or received since osquery started
    events = IntegerField()
    # Publisher only: number of runloop restarts
    refreshes = IntegerField()
    # 1 if the publisher or subscriber is active else 0
    active = IntegerField()

    class Meta:
        table_name = "osquery_events"
