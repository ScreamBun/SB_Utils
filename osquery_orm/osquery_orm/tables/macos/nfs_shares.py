"""
OSQuery nfs_shares ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class NfsShares(BaseModel):
    """
    NFS shares exported by the host.
    """
    # Filesystem path to the share
    share = TextField()
    # Options string set on the export share
    options = TextField()
    # 1 if the share is exported readonly else 0
    readonly = IntegerField()

    class Meta:
        table_name = "nfs_shares"
