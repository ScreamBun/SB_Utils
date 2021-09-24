"""
OSQuery fbsd_kmods ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class FbsdKmods(BaseModel):
    """
    Loaded FreeBSD kernel modules.
    """
    # Module name
    name = TextField()
    # Size of module content
    size = IntegerField()
    # Module reverse dependencies
    refs = IntegerField()
    # Kernel module address
    address = TextField()

    class Meta:
        table_name = "fbsd_kmods"
