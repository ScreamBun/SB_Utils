"""
OSQuery process_open_sockets ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class ProcessOpenSockets(BaseModel):
    """
    Processes which have open network sockets on the system.
    Examples:
        select * from process_open_sockets where pid = 1
    """
    # Process (or thread) ID
    pid = IntegerField()  # {'index': True}
    # Socket file descriptor number
    fd = BigIntegerField()
    # Socket handle or inode number
    socket = BigIntegerField()
    # Network protocol (IPv4, IPv6)
    family = IntegerField()
    # Transport protocol (TCP/UDP)
    protocol = IntegerField()
    # Socket local address
    local_address = TextField()
    # Socket remote address
    remote_address = TextField()
    # Socket local port
    local_port = IntegerField()
    # Socket remote port
    remote_port = IntegerField()
    # For UNIX sockets (family=AF_UNIX), the domain path
    path = TextField()

    class Meta:
        table_name = "process_open_sockets"


# OS specific properties for Linux_MacOS_Windows
class Linux_MacOS_Windows_ProcessOpenSockets(ProcessOpenSockets):
    # TCP socket state
    state = TextField()


# OS specific properties for Linux
class Linux_ProcessOpenSockets(Linux_MacOS_Windows_ProcessOpenSockets):
    # The inode number of the network namespace
    net_namespace = TextField()
