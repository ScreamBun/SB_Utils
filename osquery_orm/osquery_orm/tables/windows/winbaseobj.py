"""
OSQuery winbaseobj ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Winbaseobj(BaseModel):
    """
    Lists named Windows objects in the default object directories, across all terminal services sessions.  Example Windows ojbect types include Mutexes, Events, Jobs and Semaphors.
    Examples:
        select object_name, object_type from winbaseobj
        select * from winbaseobj where type='Mutant'
    """
    # Terminal Services Session Id
    session_id = IntegerField()
    # Object Name
    object_name = TextField()
    # Object Type
    object_type = TextField()

    class Meta:
        table_name = "winbaseobj"
