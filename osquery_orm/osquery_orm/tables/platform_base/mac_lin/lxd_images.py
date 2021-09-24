"""
OSQuery lxd_images ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class LxdImages(BaseModel):
    """
    LXD images information.
    Examples:
        select * from lxd_images
        select * from lxd_images where id = '0931b693c8'
        select * from lxd_images where id = '0931b693c877ef357b9e17b3195ae952a2450873923ffd2b34b60836ea730cfa'
    """
    # Image ID
    id = TextField()  # {'index': True}
    # Target architecture for the image
    architecture = TextField()
    # OS on which image is based
    os = TextField()
    # OS release version on which the image is based
    release = TextField()
    # Image description
    description = TextField()
    # Comma-separated list of image aliases
    aliases = TextField()
    # Filename of the image file
    filename = TextField()
    # Size of image in bytes
    size = BigIntegerField()
    # Whether the image auto-updates (1) or not (0)
    auto_update = IntegerField()
    # Whether image is cached (1) or not (0)
    cached = IntegerField()
    # Whether image is public (1) or not (0)
    public = IntegerField()
    # ISO time of image creation
    created_at = TextField()
    # ISO time of image expiration
    expires_at = TextField()
    # ISO time of image upload
    uploaded_at = TextField()
    # ISO time for the most recent use of this image in terms of container spawn
    last_used_at = TextField()
    # Server for image update
    update_source_server = TextField()
    # Protocol used for image information update and image import from source server
    update_source_protocol = TextField()
    # Certificate for update source server
    update_source_certificate = TextField()
    # Alias of image at update source server
    update_source_alias = TextField()

    class Meta:
        table_name = "lxd_images"
