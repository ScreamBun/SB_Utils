"""
OSQuery last ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Last(BaseModel):
    """
    System logins and logouts.
    """
    username = TextField(help_text="Entry username")
    tty = TextField(help_text="Entry terminal")
    pid = IntegerField(help_text="Process (or thread) ID")
    type = IntegerField(help_text="Entry type, according to ut_type types (utmp.h)")
    time = IntegerField(help_text="Entry timestamp")
    host = TextField(help_text="Entry hostname")

    class Meta:
        table_name = "last"
