"""
OSQuery lxd_instance_config ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class LxdInstanceConfig(BaseModel):
    """
    LXD instance configuration information.
    Examples:
        select * from lxd_instance_config where name = 'hello'
    """
    # Instance name
    name = TextField()  # {'index': True, 'required': True}
    # Configuration parameter name
    key = TextField()
    # Configuration parameter value
    value = TextField()

    class Meta:
        table_name = "lxd_instance_config"
