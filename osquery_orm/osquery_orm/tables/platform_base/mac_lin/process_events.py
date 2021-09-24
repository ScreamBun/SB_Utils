"""
OSQuery process_events ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class ProcessEvents(BaseModel):
    """
    Track time/action process executions.
    """
    # Process (or thread) ID
    pid = BigIntegerField()
    # Path of executed file
    path = TextField()
    # File mode permissions
    mode = TextField()
    # Command line arguments (argv)
    cmdline = TextField()
    # Actual size (bytes) of command line arguments
    cmdline_size = BigIntegerField()  # {'hidden': True}
    # Environment variables delimited by spaces
    env = TextField()  # {'aliases': ['environment'], 'hidden': True}
    # Number of environment variables
    env_count = BigIntegerField()  # {'aliases': ['environment_count'], 'hidden': True}
    # Actual size (bytes) of environment list
    env_size = BigIntegerField()  # {'aliases': ['environment_size'], 'hidden': True}
    # The process current working directory
    cwd = TextField()
    # Audit User ID at process start
    auid = BigIntegerField()
    # User ID at process start
    uid = BigIntegerField()
    # Effective user ID at process start
    euid = BigIntegerField()
    # Group ID at process start
    gid = BigIntegerField()
    # Effective group ID at process start
    egid = BigIntegerField()
    # File owner user ID
    owner_uid = BigIntegerField()
    # File owner group ID
    owner_gid = BigIntegerField()
    # File last access in UNIX time
    atime = BigIntegerField()  # {'aliases': ['access_time']}
    # File modification in UNIX time
    mtime = BigIntegerField()  # {'aliases': ['modify_time']}
    # File last metadata change in UNIX time
    ctime = BigIntegerField()  # {'aliases': ['change_time']}
    # File creation in UNIX time
    btime = BigIntegerField()  # {'aliases': ['create_time']}
    # List of structures that overflowed
    overflows = TextField()  # {'hidden': True}
    # Process parent's PID, or -1 if cannot be determined.
    parent = BigIntegerField()
    # Time of execution in UNIX time
    time = BigIntegerField()
    # Time of execution in system uptime
    uptime = BigIntegerField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "process_events"


# OS specific properties for MacOS
class MacOS_ProcessEvents(ProcessEvents):
    # OpenBSM Attribute: Status of the process
    status = BigIntegerField()


# OS specific properties for Linux
class Linux_ProcessEvents(ProcessEvents):
    # Filesystem user ID at process start
    fsuid = BigIntegerField()
    # Saved user ID at process start
    suid = BigIntegerField()
    # Filesystem group ID at process start
    fsgid = BigIntegerField()
    # Saved group ID at process start
    sgid = BigIntegerField()
    # Syscall name: fork, vfork, clone, execve, execveat
    syscall = TextField()
