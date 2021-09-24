"""
OSQuery authorization_mechanisms ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class AuthorizationMechanisms(BaseModel):
    """
    OS X Authorization mechanisms database.
    Examples:
        select * from authorization_mechanisms;
        select * from authorization_mechanisms where label = 'system.login.console';
        select * from authorization_mechanisms where label = 'authenticate';
    """
    # Label of the authorization right
    label = TextField()  # {'index': True}
    # Authorization plugin name
    plugin = TextField()
    # Name of the mechanism that will be called
    mechanism = TextField()
    # If privileged it will run as root, else as an anonymous user
    privileged = TextField()
    # The whole string entry
    entry = TextField()

    class Meta:
        table_name = "authorization_mechanisms"
