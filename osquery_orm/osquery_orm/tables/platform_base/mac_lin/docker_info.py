"""
OSQuery docker_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class DockerInfo(BaseModel):
    """
    Docker system information.
    Examples:
        select * from docker_info
    """
    # Docker system ID
    id = TextField()
    # Total number of containers
    containers = IntegerField()
    # Number of containers currently running
    containers_running = IntegerField()
    # Number of containers in paused state
    containers_paused = IntegerField()
    # Number of containers in stopped state
    containers_stopped = IntegerField()
    # Number of images
    images = IntegerField()
    # Storage driver
    storage_driver = TextField()
    # 1 if memory limit support is enabled. 0 otherwise
    memory_limit = IntegerField()
    # 1 if swap limit support is enabled. 0 otherwise
    swap_limit = IntegerField()
    # 1 if kernel memory limit support is enabled. 0 otherwise
    kernel_memory = IntegerField()
    # 1 if CPU Completely Fair Scheduler (CFS) period support is enabled. 0 otherwise
    cpu_cfs_period = IntegerField()
    # 1 if CPU Completely Fair Scheduler (CFS) quota support is enabled. 0 otherwise
    cpu_cfs_quota = IntegerField()
    # 1 if CPU share weighting support is enabled. 0 otherwise
    cpu_shares = IntegerField()
    # 1 if CPU set selection support is enabled. 0 otherwise
    cpu_set = IntegerField()
    # 1 if IPv4 forwarding is enabled. 0 otherwise
    ipv4_forwarding = IntegerField()
    # 1 if bridge netfilter iptables is enabled. 0 otherwise
    bridge_nf_iptables = IntegerField()
    # 1 if bridge netfilter ip6tables is enabled. 0 otherwise
    bridge_nf_ip6tables = IntegerField()
    # 1 if Out-of-memory kill is disabled. 0 otherwise
    oom_kill_disable = IntegerField()
    # Logging driver
    logging_driver = TextField()
    # Control groups driver
    cgroup_driver = TextField()
    # Kernel version
    kernel_version = TextField()
    # Operating system
    os = TextField()
    # Operating system type
    os_type = TextField()
    # Hardware architecture
    architecture = TextField()
    # Number of CPUs
    cpus = IntegerField()
    # Total memory
    memory = BigIntegerField()
    # HTTP proxy
    http_proxy = TextField()
    # HTTPS proxy
    https_proxy = TextField()
    # Comma-separated list of domain extensions proxy should not be used for
    no_proxy = TextField()
    # Name of the docker host
    name = TextField()
    # Server version
    server_version = TextField()
    # Docker root directory
    root_dir = TextField()

    class Meta:
        table_name = "docker_info"
