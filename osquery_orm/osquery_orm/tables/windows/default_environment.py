"""
OSQuery default_environment ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class DefaultEnvironment(BaseModel):
    """
    Default environment variables and values.
    """
    # Name of the environment variable
    variable = TextField()
    # Value of the environment variable
    value = TextField()
    # 1 if the variable needs expanding, 0 otherwise
    expand = IntegerField()

    class Meta:
        table_name = "default_environment"
