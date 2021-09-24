"""
OSQuery chocolatey_packages ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class ChocolateyPackages(BaseModel):
    """
    Chocolatey packages installed in a system.
    """
    # Package display name
    name = TextField()
    # Package-supplied version
    version = TextField()
    # Package-supplied summary
    summary = TextField()
    # Optional package author
    author = TextField()
    # License under which package is launched
    license = TextField()
    # Path at which this package resides
    path = TextField()

    class Meta:
        table_name = "chocolatey_packages"
