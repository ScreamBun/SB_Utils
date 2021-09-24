"""
OSQuery ie_extensions ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class IeExtensions(BaseModel):
    """
    Internet Explorer browser extensions.
    """
    # Extension display name
    name = TextField()
    # Extension identifier
    registry_path = TextField()
    # Version of the executable
    version = TextField()
    # Path to executable
    path = TextField()

    class Meta:
        table_name = "ie_extensions"
