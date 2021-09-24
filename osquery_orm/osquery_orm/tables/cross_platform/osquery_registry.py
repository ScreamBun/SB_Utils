"""
OSQuery osquery_registry ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class OsqueryRegistry(BaseModel):
    """
    List the osquery registry plugins.
    """
    # Name of the osquery registry
    registry = TextField()
    # Name of the plugin item
    name = TextField()
    # Extension route UUID (0 for core)
    owner_uuid = IntegerField()
    # 1 If the plugin is internal else 0
    internal = IntegerField()
    # 1 If this plugin is active else 0
    active = IntegerField()

    class Meta:
        table_name = "osquery_registry"
