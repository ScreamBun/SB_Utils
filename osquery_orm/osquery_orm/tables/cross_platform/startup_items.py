"""
OSQuery startup_items ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class StartupItems(BaseModel):
    """
    Applications and binaries set as user/login startup items.
    """
    # Name of startup item
    name = TextField()
    # Path of startup item
    path = TextField()
    # Arguments provided to startup executable
    args = TextField()
    # Startup Item or Login Item
    type = TextField()
    # Directory or plist containing startup item
    source = TextField()
    # Startup status; either enabled or disabled
    status = TextField()
    # The user associated with the startup item
    username = TextField()

    class Meta:
        table_name = "startup_items"
