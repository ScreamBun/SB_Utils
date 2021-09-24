"""
OSQuery portage_packages ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class PortagePackages(BaseModel):
    """
    List of currently installed packages.
    """
    # Package name
    package = TextField()
    # The version which are affected by the use flags, empty means all
    version = TextField()
    # The slot used by package
    slot = TextField()
    # Unix time when package was built
    build_time = BigIntegerField()
    # From which repository the ebuild was used
    repository = TextField()
    # The eapi for the ebuild
    eapi = BigIntegerField()
    # The size of the package
    size = BigIntegerField()
    # If package is in the world file
    world = IntegerField()

    class Meta:
        table_name = "portage_packages"
