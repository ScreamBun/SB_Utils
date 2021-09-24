"""
OSQuery package_install_history ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class PackageInstallHistory(BaseModel):
    """
    OS X package install history.
    """
    # Label packageIdentifiers
    package_id = TextField()
    # Label date as UNIX timestamp
    time = IntegerField()
    # Package display name
    name = TextField()
    # Package display version
    version = TextField()
    # Install source: usually the installer process name
    source = TextField()
    # Package content_type (optional)
    content_type = TextField()

    class Meta:
        table_name = "package_install_history"
