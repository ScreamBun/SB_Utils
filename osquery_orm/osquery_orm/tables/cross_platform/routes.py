"""
OSQuery routes ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Routes(BaseModel):
    """
    The active route table for the host system.
    """
    # Destination IP address
    destination = TextField()
    # Netmask length
    netmask = IntegerField()
    # Route gateway
    gateway = TextField()
    # Route source
    source = TextField()
    # Flags to describe route
    flags = IntegerField()
    # Route local interface
    interface = TextField()
    # Maximum Transmission Unit for the route
    mtu = IntegerField()
    # Cost of route. Lowest is preferred
    metric = IntegerField()
    # Type of route
    type = TextField()  # {'additional': True}

    class Meta:
        table_name = "routes"


# OS specific properties for Posix
class Posix_Routes(Routes):
    # Max hops expected
    hopcount = IntegerField()
