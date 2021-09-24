"""
OSQuery atom_packages ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class AtomPackages(BaseModel):
    """
    Lists all atom packages in a directory or globally installed in a system.
    Examples:
        select * from atom_packages
    """
    # Package display name
    name = TextField()
    # Package supplied version
    version = TextField()
    # Package supplied description
    description = TextField()
    # Package's package.json path
    path = TextField()
    # License for package
    license = TextField()
    # Package supplied homepage
    homepage = TextField()
    # The local user that owns the plugin
    uid = BigIntegerField()  # {'index': True}

    class Meta:
        table_name = "atom_packages"
