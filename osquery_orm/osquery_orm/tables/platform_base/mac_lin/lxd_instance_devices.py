"""
OSQuery lxd_instance_devices ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class LxdInstanceDevices(BaseModel):
    """
    LXD instance devices information.
    Examples:
        select * from lxd_instance_devices where name = 'hello'
    """
    # Instance name
    name = TextField()  # {'index': True, 'required': True}
    # Name of the device
    device = TextField()
    # Device type
    device_type = TextField()
    # Device info param name
    key = TextField()
    # Device info param value
    value = TextField()

    class Meta:
        table_name = "lxd_instance_devices"
