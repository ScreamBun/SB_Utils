"""
OSQuery pkg_packages ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class PkgPackages(BaseModel):
    """
    pkgng packages that are currently installed on the host system.
    """
    # Package name
    name = TextField()
    # Package version
    version = TextField()
    # Package size in bytes
    flatsize = BigIntegerField()
    # Architecture(s) supported
    arch = TextField()

    class Meta:
        table_name = "pkg_packages"
