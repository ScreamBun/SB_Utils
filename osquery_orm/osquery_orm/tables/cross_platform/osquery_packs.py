"""
OSQuery osquery_packs ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class OsqueryPacks(BaseModel):
    """
    Information about the current query packs that are loaded in osquery.
    """
    # The given name for this query pack
    name = TextField()
    # Platforms this query is supported on
    platform = TextField()
    # Minimum osquery version that this query will run on
    version = TextField()
    # Shard restriction limit, 1-100, 0 meaning no restriction
    shard = IntegerField()
    # The number of times that the discovery query used cached values since the last time the config was reloaded
    discovery_cache_hits = IntegerField()
    # The number of times that the discovery queries have been executed since the last time the config was reloaded
    discovery_executions = IntegerField()
    # Whether this pack is active (the version, platform and discovery queries match) yes=1, no=0.
    active = IntegerField()

    class Meta:
        table_name = "osquery_packs"
