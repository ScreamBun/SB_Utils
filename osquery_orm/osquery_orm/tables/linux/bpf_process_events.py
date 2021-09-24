"""
OSQuery bpf_process_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class BpfProcessEvents(BaseModel):
    """
    Track time/action process executions.
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
    # Binary path
    path = TextField()
    # Current working directory
    cwd = TextField()
    # Command line arguments
    cmdline = TextField()
    # How much time was spent inside the syscall (nsecs)
    duration = IntegerField()
    # Command line arguments, in JSON format
    json_cmdline = TextField()  # {'hidden': True}
    # The nsecs uptime timestamp as obtained from BPF
    ntime = TextField()
    # Time of execution in UNIX time
    time = BigIntegerField()  # {'hidden': True}
    # Event ID
    eid = IntegerField()  # {'hidden': True}

    class Meta:
        table_name = "bpf_process_events"
