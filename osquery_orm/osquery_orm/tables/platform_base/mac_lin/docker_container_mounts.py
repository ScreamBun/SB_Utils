"""
OSQuery docker_container_mounts ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class DockerContainerMounts(BaseModel):
    """
    Docker container mounts.
    Examples:
        select * from docker_container_mounts
        select * from docker_container_mounts where id = '1234567890abcdef'
        select * from docker_container_mounts where id = '11b2399e1426d906e62a0c357650e363426d6c56dbe2f35cbaa9b452250e3355'
    """
    # Container ID
    id = TextField()  # {'index': True}
    # Type of mount (bind, volume)
    type = TextField()
    # Optional mount name
    name = TextField()  # {'index': True}
    # Source path on host
    source = TextField()
    # Destination path inside container
    destination = TextField()
    # Driver providing the mount
    driver = TextField()
    # Mount options (rw, ro)
    mode = TextField()
    # 1 if read/write. 0 otherwise
    rw = IntegerField()
    # Mount propagation
    propagation = TextField()

    class Meta:
        table_name = "docker_container_mounts"
