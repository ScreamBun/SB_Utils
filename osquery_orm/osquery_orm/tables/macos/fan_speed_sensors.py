"""
OSQuery fan_speed_sensors ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class FanSpeedSensors(BaseModel):
    """
    Fan speeds.
    """
    # Fan number
    fan = TextField()
    # Fan name
    name = TextField()
    # Actual speed
    actual = IntegerField()
    # Minimum speed
    min = IntegerField()
    # Maximum speed
    max = IntegerField()
    # Target speed
    target = IntegerField()

    class Meta:
        table_name = "fan_speed_sensors"
