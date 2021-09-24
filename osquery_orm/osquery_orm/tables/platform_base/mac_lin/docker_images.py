"""
OSQuery docker_images ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class DockerImages(BaseModel):
    """
    Docker images information.
    Examples:
        select * from docker_images
        select * from docker_images where id = '6a2f32de169d'
        select * from docker_images where id = '6a2f32de169d14e6f8a84538eaa28f2629872d7d4f580a303b296c60db36fbd7'
    """
    # Image ID
    id = TextField()
    # Time of creation as UNIX time
    created = BigIntegerField()
    # Size of image in bytes
    size_bytes = BigIntegerField()
    # Comma-separated list of repository tags
    tags = TextField()

    class Meta:
        table_name = "docker_images"
