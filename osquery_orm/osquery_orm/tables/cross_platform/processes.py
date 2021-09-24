"""
OSQuery processes ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Processes(BaseModel):
    """
    All running processes on the host system.
    Examples:
        select * from processes where pid = 1
    """
    # Process (or thread) ID
    pid = BigIntegerField()  # {'index': True}
    # The process path or shorthand argv[0]
    name = TextField()
    # Path to executed binary
    path = TextField()
    # Complete argv
    cmdline = TextField()
    # Process state
    state = TextField()
    # Process current working directory
    cwd = TextField()
    # Process virtual root directory
    root = TextField()
    # Unsigned user ID
    uid = BigIntegerField()
    # Unsigned group ID
    gid = BigIntegerField()
    # Unsigned effective user ID
    euid = BigIntegerField()
    # Unsigned effective group ID
    egid = BigIntegerField()
    # Unsigned saved user ID
    suid = BigIntegerField()
    # Unsigned saved group ID
    sgid = BigIntegerField()
    # The process path exists yes=1, no=0, unknown=-1
    on_disk = IntegerField()
    # Bytes of unpageable memory used by process
    wired_size = BigIntegerField()
    # Bytes of private memory used by process
    resident_size = BigIntegerField()
    # Total virtual memory size
    total_size = BigIntegerField()  # {'aliases': ['phys_footprint']}
    # CPU time in milliseconds spent in user space
    user_time = BigIntegerField()
    # CPU time in milliseconds spent in kernel space
    system_time = BigIntegerField()
    # Bytes read from disk
    disk_bytes_read = BigIntegerField()
    # Bytes written to disk
    disk_bytes_written = BigIntegerField()
    # Process start time in seconds since Epoch, in case of error -1
    start_time = BigIntegerField()
    # Process parent's PID
    parent = BigIntegerField()
    # Process group
    pgroup = BigIntegerField()
    # Number of threads used by process
    threads = IntegerField()
    # Process nice level (-20 to 20, default 0)
    nice = IntegerField()

    class Meta:
        table_name = "processes"


# OS specific properties for Windows
class Windows_Processes(Processes):
    # Process uses elevated token yes=1, no=0
    elevated_token = IntegerField()
    # Process is secure (IUM) yes=1, no=0
    secure_process = IntegerField()
    # The protection type of the process
    protection_type = TextField()
    # Process is virtual (e.g. System, Registry, vmmem) yes=1, no=0
    virtual_process = IntegerField()
    # Elapsed time in seconds this process has been running.
    elapsed_time = BigIntegerField()
    # Total number of handles that the process has open. This number is the sum of the handles currently opened by each thread in the process.
    handle_count = BigIntegerField()
    # Returns elapsed time that all of the threads of this process used the processor to execute instructions in 100 nanoseconds ticks.
    percent_processor_time = BigIntegerField()


# OS specific properties for MacOS
class MacOS_Processes(Processes):
    # A 64bit pid that is never reused. Returns -1 if we couldn't gather them from the system.
    upid = BigIntegerField()
    # The 64bit parent pid that is never reused. Returns -1 if we couldn't gather them from the system.
    uppid = BigIntegerField()
    # Indicates the specific processor designed for installation.
    cpu_type = IntegerField()
    # Indicates the specific processor on which an entry may be used.
    cpu_subtype = IntegerField()
