"""
OSQuery crashes ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Crashes(BaseModel):
    """
    Application, System, and Mobile App crash logs.
    Examples:
        select * from users join crashes using (uid)
    """
    # Type of crash log
    type = TextField()
    # Process (or thread) ID of the crashed process
    pid = BigIntegerField()
    # Path to the crashed process
    path = TextField()
    # Location of log file
    crash_path = TextField()  # {'index': True}
    # Identifier of the crashed process
    identifier = TextField()
    # Version info of the crashed process
    version = TextField()
    # Parent PID of the crashed process
    parent = BigIntegerField()
    # Process responsible for the crashed process
    responsible = TextField()
    # User ID of the crashed process
    uid = IntegerField()  # {'index': True}
    # Date/Time at which the crash occurred
    datetime = TextField()
    # Thread ID which crashed
    crashed_thread = BigIntegerField()
    # Most recent frame from the stack trace
    stack_trace = TextField()
    # Exception type of the crash
    exception_type = TextField()
    # Exception codes from the crash
    exception_codes = TextField()
    # Exception notes from the crash
    exception_notes = TextField()
    # The value of the system registers
    registers = TextField()

    class Meta:
        table_name = "crashes"
