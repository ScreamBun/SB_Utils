"""
OSQuery alf_exceptions ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class AlfExceptions(BaseModel):
    """
    OS X application layer firewall (ALF) service exceptions.
    """
    # Path to the executable that is excepted
    path = TextField()
    # Firewall exception state
    state = IntegerField()

    class Meta:
        table_name = "alf_exceptions"
