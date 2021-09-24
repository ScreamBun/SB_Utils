"""
OSQuery wmi_bios_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class WmiBiosInfo(BaseModel):
    """
    Lists important information from the system bios.
    Examples:
        select * from wmi_bios_info
        select * from wmi_bios_info where name = 'AMTControl'
    """
    # Name of the Bios setting
    name = TextField()
    # Value of the Bios setting
    value = TextField()

    class Meta:
        table_name = "wmi_bios_info"
