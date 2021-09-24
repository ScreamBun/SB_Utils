"""
OSQuery docker_container_processes ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, DoubleField, BigIntegerField, TextField


class DockerContainerProcesses(BaseModel):
    """
    Docker container processes.
    Examples:
        select * from docker_container_processes where id = '1234567890abcdef'
        select * from docker_container_processes where id = '11b2399e1426d906e62a0c357650e363426d6c56dbe2f35cbaa9b452250e3355'
    """
    # Container ID
    id = TextField()  # {'index': True, 'required': True}
    # Process ID
    pid = BigIntegerField()  # {'index': True}
    # The process path or shorthand argv[0]
    name = TextField()
    # Complete argv
    cmdline = TextField()
    # Process state
    state = TextField()
    # User ID
    uid = BigIntegerField()
    # Group ID
    gid = BigIntegerField()
    # Effective user ID
    euid = BigIntegerField()
    # Effective group ID
    egid = BigIntegerField()
    # Saved user ID
    suid = BigIntegerField()
    # Saved group ID
    sgid = BigIntegerField()
    # Bytes of unpageable memory used by process
    wired_size = BigIntegerField()
    # Bytes of private memory used by process
    resident_size = BigIntegerField()
    # Total virtual memory size
    total_size = BigIntegerField()  # {'aliases': ['phys_footprint']}
    # Process start in seconds since boot (non-sleeping)
    start_time = BigIntegerField()
    # Process parent's PID
    parent = BigIntegerField()
    # Process group
    pgroup = BigIntegerField()
    # Number of threads used by process
    threads = IntegerField()
    # Process nice level (-20 to 20, default 0)
    nice = IntegerField()
    # User name
    user = TextField()
    # Cumulative CPU time. [DD-]HH:MM:SS format
    time = TextField()
    # CPU utilization as percentage
    cpu = DoubleField()
    # Memory utilization as percentage
    mem = DoubleField()

    class Meta:
        table_name = "docker_container_processes"
