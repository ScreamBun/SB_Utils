"""
OSQuery osquery_extensions ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class OsqueryExtensions(BaseModel):
    """
    List of active osquery extensions.
    """
    # The transient ID assigned for communication
    uuid = BigIntegerField()
    # Extension's name
    name = TextField()
    # Extension's version
    version = TextField()
    # osquery SDK version used to build the extension
    sdk_version = TextField()
    # Path of the extension's Thrift connection or library path
    path = TextField()
    # SDK extension type: extension or module
    type = TextField()

    class Meta:
        table_name = "osquery_extensions"
