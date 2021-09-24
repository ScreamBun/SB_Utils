"""
OSQuery process_file_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class ProcessFileEvents(BaseModel):
    """
    A File Integrity Monitor implementation using the audit service.
    """
    # Operation type
    operation = TextField()
    # Process ID
    pid = BigIntegerField()
    # Parent process ID
    ppid = BigIntegerField()
    # Time of execution in UNIX time
    time = BigIntegerField()
    # The executable path
    executable = TextField()
    # True if this is a partial event (i.e.: this process existed before we started osquery)
    partial = TextField()
    # The current working directory of the process
    cwd = TextField()
    # The path associated with the event
    path = TextField()
    # The canonical path associated with the event
    dest_path = TextField()
    # The uid of the process performing the action
    uid = TextField()
    # The gid of the process performing the action
    gid = TextField()
    # Audit user ID of the process using the file
    auid = TextField()
    # Effective user ID of the process using the file
    euid = TextField()
    # Effective group ID of the process using the file
    egid = TextField()
    # Filesystem user ID of the process using the file
    fsuid = TextField()
    # Filesystem group ID of the process using the file
    fsgid = TextField()
    # Saved user ID of the process using the file
    suid = TextField()
    # Saved group ID of the process using the file
    sgid = TextField()
    # Time of execution in system uptime
    uptime = BigIntegerField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "process_file_events"
