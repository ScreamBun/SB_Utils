"""
OSQuery nfs_shares ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField, IntegerField


class NfsShares(BaseModel):
    """
    NFS shares exported by the host.
    """
    share = TextField(help_text="Filesystem path to the share")
    options = TextField(help_text="Options string set on the export share")
    readonly = IntegerField(help_text="1 if the share is exported readonly else 0")

    class Meta:
        table_name = "nfs_shares"
