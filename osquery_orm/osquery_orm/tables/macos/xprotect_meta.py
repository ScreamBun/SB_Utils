"""
OSQuery xprotect_meta ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class XprotectMeta(BaseModel):
    """
    Database of the machine's XProtect browser-related signatures.
    """
    # Browser plugin or extension identifier
    identifier = TextField()
    # Either plugin or extension
    type = TextField()
    # Developer identity (SHA1) of extension
    developer_id = TextField()
    # The minimum allowed plugin version.
    min_version = TextField()

    class Meta:
        table_name = "xprotect_meta"
