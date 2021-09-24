"""
OSQuery rpm_packages ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class RpmPackages(BaseModel):
    """
    RPM packages that are currently installed on the host system.
    """
    # RPM package name
    name = TextField()  # {'index': True}
    # Package version
    version = TextField()  # {'index': True}
    # Package release
    release = TextField()  # {'index': True}
    # Source RPM package name (optional)
    source = TextField()
    # Package size in bytes
    size = BigIntegerField()
    # SHA1 hash of the package contents
    sha1 = TextField()
    # Architecture(s) supported
    arch = TextField()  # {'index': True}
    # Package epoch value
    epoch = IntegerField()  # {'index': True}
    # When the package was installed
    install_time = IntegerField()
    # Package vendor
    vendor = TextField()
    # Package group
    package_group = TextField()

    class Meta:
        table_name = "rpm_packages"


# OS specific properties for Linux
class Linux_RpmPackages(RpmPackages):
    # Pids that contain a namespace
    pid_with_namespace = IntegerField()  # {'additional': True, 'hidden': True}
    # Mount namespace id
    mount_namespace_id = TextField()  # {'hidden': True}
