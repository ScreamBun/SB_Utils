"""
OSQuery crontab ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Crontab(BaseModel):
    """
    Line parsed values from system and user cron/tab.
    """
    # The job @event name (rare)
    event = TextField()
    # The exact minute for the job
    minute = TextField()
    # The hour of the day for the job
    hour = TextField()
    # The day of the month for the job
    day_of_month = TextField()
    # The month of the year for the job
    month = TextField()
    # The day of the week for the job
    day_of_week = TextField()
    # Raw command string
    command = TextField()
    # File parsed
    path = TextField()

    class Meta:
        table_name = "crontab"
