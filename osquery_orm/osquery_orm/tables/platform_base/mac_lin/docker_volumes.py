"""
OSQuery docker_volumes ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class DockerVolumes(BaseModel):
    """
    Docker volumes information.
    Examples:
        select * from docker_volumes
        select * from docker_volumes where name = 'btrfs'
    """
    # Volume name
    name = TextField()  # {'index': True}
    # Volume driver
    driver = TextField()
    # Mount point
    mount_point = TextField()
    # Volume type
    type = TextField()

    class Meta:
        table_name = "docker_volumes"
