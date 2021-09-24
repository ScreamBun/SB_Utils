"""
OSQuery scheduled_tasks ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class ScheduledTasks(BaseModel):
    """
    Lists all of the tasks in the Windows task scheduler.
    Examples:
        select * from scheduled_tasks
        select * from scheduled_tasks where hidden=1 and enabled=1
    """
    # Name of the scheduled task
    name = TextField()
    # Actions executed by the scheduled task
    action = TextField()
    # Path to the executable to be run
    path = TextField()
    # Whether or not the scheduled task is enabled
    enabled = IntegerField()
    # State of the scheduled task
    state = TextField()
    # Whether or not the task is visible in the UI
    hidden = IntegerField()
    # Timestamp the task last ran
    last_run_time = BigIntegerField()
    # Timestamp the task is scheduled to run next
    next_run_time = BigIntegerField()
    # Exit status message of the last task run
    last_run_message = TextField()
    # Exit status code of the last task run
    last_run_code = TextField()

    class Meta:
        table_name = "scheduled_tasks"
