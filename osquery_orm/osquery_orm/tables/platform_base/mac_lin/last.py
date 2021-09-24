"""
OSQuery last ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Last(BaseModel):
    """
    System logins and logouts.
    """
    # Entry username
    username = TextField()
    # Entry terminal
    tty = TextField()
    # Process (or thread) ID
    pid = IntegerField()
    # Entry type, according to ut_type types (utmp.h)
    type = IntegerField()
    # Entry timestamp
    time = IntegerField()
    # Entry hostname
    host = TextField()

    class Meta:
        table_name = "last"
