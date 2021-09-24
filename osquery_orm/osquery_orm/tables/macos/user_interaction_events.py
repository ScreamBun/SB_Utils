"""
OSQuery user_interaction_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField


class UserInteractionEvents(BaseModel):
    """
    Track user interaction events from macOS' event tapping framework.
    """
    # Time
    time = BigIntegerField()

    class Meta:
        table_name = "user_interaction_events"
