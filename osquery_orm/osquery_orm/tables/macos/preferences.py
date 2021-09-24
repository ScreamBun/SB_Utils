"""
OSQuery preferences ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Preferences(BaseModel):
    """
    OS X defaults and managed preferences.
    Examples:
        select * from preferences where domain = 'loginwindow'
        select preferences.* from users join preferences using (username)
    """
    # Application ID usually in com.name.product format
    domain = TextField()  # {'index': True}
    # Preference top-level key
    key = TextField()  # {'index': True}
    # Intemediate key path, includes lists/dicts
    subkey = TextField()
    # String value of most CF types
    value = TextField()
    # 1 if the value is forced/managed, else 0
    forced = IntegerField()
    # (optional) read preferences for a specific user
    username = TextField()  # {'additional': True}
    # 'current' or 'any' host, where 'current' takes precedence
    host = TextField()

    class Meta:
        table_name = "preferences"
