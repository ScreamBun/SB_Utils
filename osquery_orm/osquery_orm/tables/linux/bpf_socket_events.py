"""
OSQuery bpf_socket_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class BpfSocketEvents(BaseModel):
    """
    Track network socket opens and closes.
    """
    # Thread ID
    tid = BigIntegerField()
    # Process ID
    pid = BigIntegerField()
    # Parent process ID
    parent = BigIntegerField()
    # User ID
    uid = BigIntegerField()
    # Group ID
    gid = BigIntegerField()
    # Cgroup ID
    cid = IntegerField()
    # Exit code of the system call
    exit_code = TextField()
    # Set to 1 if one or more buffers could not be captured
    probe_error = IntegerField()
    # System call name
    syscall = TextField()
    # Path of executed file
    path = TextField()
    # The file description for the process socket
    fd = TextField()
    # The Internet protocol family ID
    family = IntegerField()
    # The socket type
    type = IntegerField()
    # The network protocol ID
    protocol = IntegerField()
    # Local address associated with socket
    local_address = TextField()
    # Remote address associated with socket
    remote_address = TextField()
    # Local network protocol port number
    local_port = IntegerField()
    # Remote network protocol port number
    remote_port = IntegerField()
    # How much time was spent inside the syscall (nsecs)
    duration = IntegerField()
    # The nsecs uptime timestamp as obtained from BPF
    ntime = TextField()
    # Time of execution in UNIX time
    time = BigIntegerField()  # {'hidden': True}
    # Event ID
    eid = IntegerField()  # {'hidden': True}

    class Meta:
        table_name = "bpf_socket_events"
