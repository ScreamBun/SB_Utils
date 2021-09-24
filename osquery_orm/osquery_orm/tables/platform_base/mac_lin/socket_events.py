"""
OSQuery socket_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class SocketEvents(BaseModel):
    """
    Track network socket opens and closes.
    """
    # The socket action (bind, listen, close)
    action = TextField()
    # Process (or thread) ID
    pid = BigIntegerField()
    # Path of executed file
    path = TextField()
    # The file description for the process socket
    fd = TextField()
    # Audit User ID
    auid = BigIntegerField()
    # The socket open attempt status
    success = IntegerField()
    # The Internet protocol family ID
    family = IntegerField()
    # The network protocol ID
    protocol = IntegerField()  # {'hidden': True}
    # Local address associated with socket
    local_address = TextField()
    # Remote address associated with socket
    remote_address = TextField()
    # Local network protocol port number
    local_port = IntegerField()
    # Remote network protocol port number
    remote_port = IntegerField()
    # The local path (UNIX domain socket only)
    socket = TextField()  # {'hidden': True}
    # Time of execution in UNIX time
    time = BigIntegerField()
    # Time of execution in system uptime
    uptime = BigIntegerField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "socket_events"
