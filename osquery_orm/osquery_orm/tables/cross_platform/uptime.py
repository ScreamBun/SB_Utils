"""
OSQuery uptime ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField


class Uptime(BaseModel):
    """
    Track time passed since last boot.
    """
    # Days of uptime
    days = IntegerField()
    # Hours of uptime
    hours = IntegerField()
    # Minutes of uptime
    minutes = IntegerField()
    # Seconds of uptime
    seconds = IntegerField()
    # Total uptime seconds
    total_seconds = BigIntegerField()

    class Meta:
        table_name = "uptime"
