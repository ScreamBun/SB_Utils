"""
OSQuery deb_packages ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class DebPackages(BaseModel):
    """
    The installed DEB package database.
    """
    # Package name
    name = TextField()
    # Package version
    version = TextField()
    # Package source
    source = TextField()
    # Package size in bytes
    size = BigIntegerField()
    # Package architecture
    arch = TextField()
    # Package revision
    revision = TextField()
    # Package status
    status = TextField()
    # Package maintainer
    maintainer = TextField()
    # Package section
    section = TextField()
    # Package priority
    priority = TextField()

    class Meta:
        table_name = "deb_packages"


# OS specific properties for Linux
class Linux_DebPackages(DebPackages):
    # Pids that contain a namespace
    pid_with_namespace = IntegerField()  # {'additional': True, 'hidden': True}
    # Mount namespace id
    mount_namespace_id = TextField()  # {'hidden': True}
