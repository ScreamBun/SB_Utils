"""
OSQuery seccomp_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class SeccompEvents(BaseModel):
    """
    A virtual table that tracks seccomp events.
    """
    # Time of execution in UNIX time
    time = BigIntegerField()
    # Time of execution in system uptime
    uptime = BigIntegerField()
    # Audit user ID (loginuid) of the user who started the analyzed process
    auid = BigIntegerField()
    # User ID of the user who started the analyzed process
    uid = BigIntegerField()
    # Group ID of the user who started the analyzed process
    gid = BigIntegerField()
    # Session ID of the session from which the analyzed process was invoked
    ses = BigIntegerField()
    # Process ID
    pid = BigIntegerField()
    # Command-line name of the command that was used to invoke the analyzed process
    comm = TextField()
    # The path to the executable that was used to invoke the analyzed process
    exe = TextField()
    # Signal value sent to process by seccomp
    sig = BigIntegerField()
    # Information about the CPU architecture
    arch = TextField()
    # Type of the system call
    syscall = TextField()
    # Is system call in compatibility mode
    compat = BigIntegerField()
    # Instruction pointer value
    ip = TextField()
    # The seccomp action
    code = TextField()

    class Meta:
        table_name = "seccomp_events"
