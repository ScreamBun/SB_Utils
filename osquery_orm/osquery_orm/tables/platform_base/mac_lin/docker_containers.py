"""
OSQuery docker_containers ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class DockerContainers(BaseModel):
    """
    Docker containers information.
    Examples:
        select * from docker_containers where id = '11b2399e1426d906e62a0c357650e363426d6c56dbe2f35cbaa9b452250e3355'
        select * from docker_containers where name = '/hello'
    """
    # Container ID
    id = TextField()  # {'index': True}
    # Container name
    name = TextField()  # {'index': True}
    # Docker image (name) used to launch this container
    image = TextField()
    # Docker image ID
    image_id = TextField()
    # Command with arguments
    command = TextField()
    # Time of creation as UNIX time
    created = BigIntegerField()
    # Container state (created, restarting, running, removing, paused, exited, dead)
    state = TextField()
    # Container status information
    status = TextField()
    # Identifier of the initial process
    pid = BigIntegerField()
    # Container path
    path = TextField()
    # Container entrypoint(s)
    config_entrypoint = TextField()
    # Container start time as string
    started_at = TextField()
    # Container finish time as string
    finished_at = TextField()
    # Is the container privileged
    privileged = IntegerField()
    # List of container security options
    security_options = TextField()
    # Container environmental variables
    env_variables = TextField()
    # Is the root filesystem mounted as read only
    readonly_rootfs = IntegerField()

    class Meta:
        table_name = "docker_containers"


# OS specific properties for Linux
class Linux_DockerContainers(DockerContainers):
    # cgroup namespace
    cgroup_namespace = TextField()
    # IPC namespace
    ipc_namespace = TextField()
    # Mount namespace
    mnt_namespace = TextField()
    # Network namespace
    net_namespace = TextField()
    # PID namespace
    pid_namespace = TextField()
    # User namespace
    user_namespace = TextField()
    # UTS namespace
    uts_namespace = TextField()
