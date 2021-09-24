"""
OSQuery system_controls ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import TextField


class SystemControls(BaseModel):
    """
    sysctl names, values, and settings information.
    """
    # Full sysctl MIB name
    name = TextField()  # {'index': True}
    # Control MIB
    oid = TextField()  # {'additional': True}
    # Subsystem ID, control type
    subsystem = TextField()  # {'additional': True}
    # Value of setting
    current_value = TextField()
    # The MIB value set in /etc/sysctl.conf
    config_value = TextField()
    # Data type
    type = TextField()

    class Meta:
        table_name = "system_controls"


# OS specific properties for MacOS
class MacOS_SystemControls(SystemControls):
    # Specific attribute of opaque type
    field_name = TextField()
