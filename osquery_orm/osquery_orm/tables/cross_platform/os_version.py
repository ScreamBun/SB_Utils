"""
OSQuery os_version ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class OSVersion(BaseModel):
    """
    A single row containing the operating system name and version.
    """
    # Distribution or product name
    name = TextField()
    # Pretty, suitable for presentation, OS version
    version = TextField()
    # Major release version
    major = IntegerField()
    # Minor release version
    minor = IntegerField()
    # Optional patch release
    patch = IntegerField()
    # Optional build-specific or variant string
    build = TextField()
    # OS Platform or ID
    platform = TextField()
    # Closely related platforms
    platform_like = TextField()
    # OS version codename
    codename = TextField()
    # OS Architecture
    arch = TextField()

    class Meta:
        table_name = "os_version"


# OS specific properties for Windows
class Windows_OSVersion(OSVersion):
    # The install date of the OS.
    install_date = BigIntegerField()


# OS specific properties for Linux
class Linux_OSVersion(OSVersion):
    # Pids that contain a namespace
    pid_with_namespace = IntegerField()  # {'additional': True, 'hidden': True}
    # Mount namespace id
    mount_namespace_id = TextField()  # {'hidden': True}
