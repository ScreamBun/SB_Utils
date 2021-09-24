"""
OSQuery lxd_cluster ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class LxdCluster(BaseModel):
    """
    LXD cluster information.
    Examples:
        select * from lxd_cluster
    """
    # Name of the LXD server node
    server_name = TextField()
    # Whether clustering enabled (1) or not (0) on this node
    enabled = IntegerField()
    # Type of configuration parameter for this node
    member_config_entity = TextField()
    # Name of configuration parameter
    member_config_name = TextField()
    # Config key
    member_config_key = TextField()
    # Config value
    member_config_value = TextField()
    # Config description
    member_config_description = TextField()

    class Meta:
        table_name = "lxd_cluster"
