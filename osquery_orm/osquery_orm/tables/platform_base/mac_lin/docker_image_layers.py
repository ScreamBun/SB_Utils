"""
OSQuery docker_image_layers ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class DockerImageLayers(BaseModel):
    """
    Docker image layers information.
    Examples:
        select * from docker_images
        select * from docker_images where id = '6a2f32de169d'
        select * from docker_images where id = '6a2f32de169d14e6f8a84538eaa28f2629872d7d4f580a303b296c60db36fbd7'
    """
    # Image ID
    id = TextField()  # {'index': True}
    # Layer ID
    layer_id = TextField()
    # Layer Order (1 = base layer)
    layer_order = IntegerField()

    class Meta:
        table_name = "docker_image_layers"