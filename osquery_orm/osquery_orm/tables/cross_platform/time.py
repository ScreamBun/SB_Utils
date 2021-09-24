"""
OSQuery time ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Time(BaseModel):
    """
    Track current date and time in the system.
    """
    # Current weekday in the system
    weekday = TextField()
    # Current year in the system
    year = IntegerField()
    # Current month in the system
    month = IntegerField()
    # Current day in the system
    day = IntegerField()
    # Current hour in the system
    hour = IntegerField()
    # Current minutes in the system
    minutes = IntegerField()
    # Current seconds in the system
    seconds = IntegerField()
    # Current timezone in the system
    timezone = TextField()
    # Current local UNIX time in the system
    local_time = IntegerField()  # {'aliases': ['localtime']}
    # Current local timezone in the system
    local_timezone = TextField()
    # Current UNIX time in the system, converted to UTC if --utc enabled
    unix_time = IntegerField()
    # Current timestamp (log format) in the system
    timestamp = TextField()
    # Current date and time (ISO format) in the system
    datetime = TextField()  # {'aliases': ['date_time']}
    # Current time (ISO format) in the system
    iso_8601 = TextField()

    class Meta:
        table_name = "time"


# OS specific properties for Windows
class Windows_Time(Time):
    # Timestamp value in 100 nanosecond units.
    win_timestamp = BigIntegerField()
