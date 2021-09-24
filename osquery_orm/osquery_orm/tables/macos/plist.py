"""
OSQuery plist ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Plist(BaseModel):
    """
    Read and parse a plist file.
    Examples:
        select * from plist where path = '/Library/Preferences/loginwindow.plist'
    """
    # Preference top-level key
    key = TextField()
    # Intermediate key path, includes lists/dicts
    subkey = TextField()
    # String value of most CF types
    value = TextField()
    # (required) read preferences from a plist
    path = TextField()  # {'required': True}

    class Meta:
        table_name = "plist"
