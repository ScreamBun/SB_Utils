"""
OSQuery shimcache ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Shimcache(BaseModel):
    """
    Application Compatibility Cache, contains artifacts of execution.
    Examples:
        select * from shimcache;
    """
    # Execution order.
    entry = IntegerField()
    # This is the path to the executed file.
    path = TextField()
    # File Modified time.
    modified_time = IntegerField()
    # Boolean Execution flag, 1 for execution, 0 for no execution, -1 for missing (this flag does not exist on Windows 10 and higher).
    execution_flag = IntegerField()

    class Meta:
        table_name = "shimcache"
