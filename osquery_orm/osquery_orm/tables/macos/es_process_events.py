"""
OSQuery es_process_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class EsProcessEvents(BaseModel):
    """
    Process execution events from EndpointSecurity.
    """
    # Version of EndpointSecurity event
    version = IntegerField()
    # Per event sequence number
    seq_num = BigIntegerField()
    # Global sequence number
    global_seq_num = BigIntegerField()
    # Process (or thread) ID
    pid = BigIntegerField()
    # Path of executed file
    path = TextField()
    # Parent process ID
    parent = BigIntegerField()
    # Original parent process ID in case of reparenting
    original_parent = BigIntegerField()
    # Command line arguments (argv)
    cmdline = TextField()
    # Number of command line arguments
    cmdline_count = BigIntegerField()
    # Environment variables delimited by spaces
    env = TextField()
    # Number of environment variables
    env_count = BigIntegerField()
    # The process current working directory
    cwd = TextField()
    # User ID of the process
    uid = BigIntegerField()
    # Effective User ID of the process
    euid = BigIntegerField()
    # Group ID of the process
    gid = BigIntegerField()
    # Effective Group ID of the process
    egid = BigIntegerField()
    # Username
    username = TextField()
    # Signature identifier of the process
    signing_id = TextField()
    # Team identifier of thd process
    team_id = TextField()
    # Codesigning hash of the process
    cdhash = TextField()
    # Indicates if the binary is Apple signed binary (1) or not (0)
    platform_binary = IntegerField()
    # Exit code of a process in case of an exit event
    exit_code = IntegerField()
    # Process ID of a child process in case of a fork event
    child_pid = BigIntegerField()
    # Time of execution in UNIX time
    time = BigIntegerField()
    # Type of EndpointSecurity event
    event_type = TextField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "es_process_events"
