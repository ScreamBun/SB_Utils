"""
OSQuery osquery_flags ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class OsqueryFlags(BaseModel):
    """
    Configurable flags that modify osquery's behavior.
    """
    # Flag name
    name = TextField()
    # Flag type
    type = TextField()
    # Flag description
    description = TextField()
    # Flag default value
    default_value = TextField()
    # Flag value
    value = TextField()
    # Is the flag shell only?
    shell_only = IntegerField()

    class Meta:
        table_name = "osquery_flags"
