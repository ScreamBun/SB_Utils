"""
OSQuery authorizations ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Authorizations(BaseModel):
    """
    OS X Authorization rights database.
    Examples:
        select * from authorizations;
        select * from authorizations where label = 'system.login.console';
        select * from authorizations where label = 'authenticate';
        select * from authorizations where label = 'system.preferences.softwareupdate';
    """
    # Item name, usually in reverse domain format
    label = TextField()  # {'index': True}
    # Label top-level key
    modified = TextField()
    # Label top-level key
    allow_root = TextField()
    # Label top-level key
    timeout = TextField()
    # Label top-level key
    version = TextField()
    # Label top-level key
    tries = TextField()
    # Label top-level key
    authenticate_user = TextField()
    # Label top-level key
    shared = TextField()
    # Label top-level key
    comment = TextField()
    # Label top-level key
    created = TextField()
    # Label top-level key
    class_ = TextField(column_name="class")
    # Label top-level key
    session_owner = TextField()

    class Meta:
        table_name = "authorizations"
