"""
OSQuery listening_ports ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class ListeningPorts(BaseModel):
    """
    Processes with listening (bound) network sockets/ports.
    """
    # Process (or thread) ID
    pid = IntegerField()
    # Transport layer port
    port = IntegerField()
    # Transport protocol (TCP/UDP)
    protocol = IntegerField()
    # Network protocol (IPv4, IPv6)
    family = IntegerField()
    # Specific address for bind
    address = TextField()
    # Socket file descriptor number
    fd = BigIntegerField()
    # Socket handle or inode number
    socket = BigIntegerField()
    # Path for UNIX domain sockets
    path = TextField()

    class Meta:
        table_name = "listening_ports"


# OS specific properties for Linux
class Linux_ListeningPorts(ListeningPorts):
    # The inode number of the network namespace
    net_namespace = TextField()
