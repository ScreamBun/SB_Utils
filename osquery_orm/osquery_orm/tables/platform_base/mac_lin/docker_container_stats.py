"""
OSQuery docker_container_stats ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class DockerContainerStats(BaseModel):
    """
    Docker container statistics. Queries on this table take at least one second.
    Examples:
        select * from docker_container_stats where id = 'de8cfdc74c850967'
        select * from docker_container_stats where id = 'de8cfdc74c850967fd3832e128f4d12e2d5476a4aea282734bfb7e57f66fce2f'
    """
    # Container ID
    id = TextField()  # {'index': True, 'required': True}
    # Container name
    name = TextField()  # {'index': True}
    # Number of processes
    pids = IntegerField()
    # UNIX time when stats were read
    read = BigIntegerField()
    # UNIX time when stats were last read
    preread = BigIntegerField()
    # Difference between read and preread in nano-seconds
    interval = BigIntegerField()
    # Total disk read bytes
    disk_read = BigIntegerField()
    # Total disk write bytes
    disk_write = BigIntegerField()
    # Number of processors
    num_procs = IntegerField()
    # Total CPU usage
    cpu_total_usage = BigIntegerField()
    # CPU kernel mode usage
    cpu_kernelmode_usage = BigIntegerField()
    # CPU user mode usage
    cpu_usermode_usage = BigIntegerField()
    # CPU system usage
    system_cpu_usage = BigIntegerField()
    # Online CPUs
    online_cpus = IntegerField()
    # Last read total CPU usage
    pre_cpu_total_usage = BigIntegerField()
    # Last read CPU kernel mode usage
    pre_cpu_kernelmode_usage = BigIntegerField()
    # Last read CPU user mode usage
    pre_cpu_usermode_usage = BigIntegerField()
    # Last read CPU system usage
    pre_system_cpu_usage = BigIntegerField()
    # Last read online CPUs
    pre_online_cpus = IntegerField()
    # Memory usage
    memory_usage = BigIntegerField()
    # Memory maximum usage
    memory_max_usage = BigIntegerField()
    # Memory limit
    memory_limit = BigIntegerField()
    # Total network bytes read
    network_rx_bytes = BigIntegerField()
    # Total network bytes transmitted
    network_tx_bytes = BigIntegerField()

    class Meta:
        table_name = "docker_container_stats"
