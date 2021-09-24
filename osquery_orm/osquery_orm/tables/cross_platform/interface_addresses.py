"""
OSQuery interface_addresses ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import TextField


class InterfaceAddresses(BaseModel):
    """
    Network interfaces and relevant metadata.
    """
    # Interface name
    interface = TextField()
    # Specific address for interface
    address = TextField()
    # Interface netmask
    mask = TextField()
    # Broadcast address for the interface
    broadcast = TextField()
    # PtP address for the interface
    point_to_point = TextField()
    # Type of address. One of dhcp, manual, auto, other, unknown
    type = TextField()

    class Meta:
        table_name = "interface_addresses"


# OS specific properties for Windows
class Windows_InterfaceAddresses(InterfaceAddresses):
    # The friendly display name of the interface.
    friendly_name = TextField()
