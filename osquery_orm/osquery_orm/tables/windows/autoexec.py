"""
OSQuery autoexec ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Autoexec(BaseModel):
    """
    Aggregate of executables that will automatically execute on the target machine. This is an amalgamation of other tables like services, scheduled_tasks, startup_items and more.
    """
    # Path to the executable
    path = TextField()  # {'index': True}
    # Name of the program
    name = TextField()
    # Source table of the autoexec item
    source = TextField()

    class Meta:
        table_name = "autoexec"
