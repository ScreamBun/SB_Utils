"""
OSQuery rpm_package_files ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class RpmPackageFiles(BaseModel):
    """
    RPM packages that are currently installed on the host system.
    """
    # RPM package name
    package = TextField()  # {'index': True}
    # File path within the package
    path = TextField()  # {'index': True}
    # File default username from info DB
    username = TextField()
    # File default groupname from info DB
    groupname = TextField()
    # File permissions mode from info DB
    mode = TextField()
    # Expected file size in bytes from RPM info DB
    size = BigIntegerField()
    # SHA256 file digest from RPM info DB
    sha256 = TextField()

    class Meta:
        table_name = "rpm_package_files"
