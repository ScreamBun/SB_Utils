"""
OSQuery lxd_instances ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class LxdInstances(BaseModel):
    """
    LXD instances information.
    Examples:
        select * from lxd_instances
        select * from lxd_instances where name = 'hello'
    """
    # Instance name
    name = TextField()  # {'index': True}
    # Instance state (running, stopped, etc.)
    status = TextField()
    # Whether the instance is stateful(1) or not(0)
    stateful = IntegerField()
    # Whether the instance is ephemeral(1) or not(0)
    ephemeral = IntegerField()
    # ISO time of creation
    created_at = TextField()
    # ID of image used to launch this instance
    base_image = TextField()
    # Instance architecture
    architecture = TextField()
    # The OS of this instance
    os = TextField()
    # Instance description
    description = TextField()
    # Instance's process ID
    pid = IntegerField()
    # Number of processes running inside this instance
    processes = IntegerField()

    class Meta:
        table_name = "lxd_instances"
