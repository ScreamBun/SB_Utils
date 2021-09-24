"""
OSQuery system_extensions ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class SystemExtensions(BaseModel):
    """
    macOS (>= 10.15) system extension table.
    Examples:
        select * from system_extensions
    """
    # Original path of system extension
    path = TextField()
    # Extension unique id
    UUID = TextField()
    # System extension state
    state = TextField()
    # Identifier name
    identifier = TextField()
    # System extension version
    version = TextField()
    # System extension category
    category = TextField()
    # System extension bundle path
    bundle_path = TextField()
    # Signing team ID
    team = TextField()
    # 1 if managed by MDM system extension payload configuration, 0 otherwise
    mdm_managed = IntegerField()

    class Meta:
        table_name = "system_extensions"
