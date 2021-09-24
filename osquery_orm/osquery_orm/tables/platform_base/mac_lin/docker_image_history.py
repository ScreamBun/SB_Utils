"""
OSQuery docker_image_history ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class DockerImageHistory(BaseModel):
    """
    Docker image history information.
    Examples:
        select * from docker_image_history
        select * from docker_image_history where id = '6a2f32de169d'
        select * from docker_image_history where id = '6a2f32de169d14e6f8a84538eaa28f2629872d7d4f580a303b296c60db36fbd7'
    """
    # Image ID
    id = TextField()  # {'index': True}
    # Time of creation as UNIX time
    created = BigIntegerField()
    # Size of instruction in bytes
    size = BigIntegerField()
    # Created by instruction
    created_by = TextField()
    # Comma-separated list of tags
    tags = TextField()
    # Instruction comment
    comment = TextField()

    class Meta:
        table_name = "docker_image_history"
