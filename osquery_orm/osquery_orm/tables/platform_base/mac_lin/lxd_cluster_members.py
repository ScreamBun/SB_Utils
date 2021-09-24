"""
OSQuery lxd_cluster_members ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class LxdClusterMembers(BaseModel):
    """
    LXD cluster members information.
    Examples:
        select * from lxd_cluster_members
    """
    # Name of the LXD server node
    server_name = TextField()
    # URL of the node
    url = TextField()
    # Whether the server is a database node (1) or not (0)
    database = IntegerField()
    # Status of the node (Online/Offline)
    status = TextField()
    # Message from the node (Online/Offline)
    message = TextField()

    class Meta:
        table_name = "lxd_cluster_members"
