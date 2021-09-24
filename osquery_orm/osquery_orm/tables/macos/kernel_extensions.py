"""
OSQuery kernel_extensions ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class KernelExtensions(BaseModel):
    """
    OS X's kernel extensions, both loaded and within the load search path.
    """
    # Extension load tag or index
    idx = IntegerField()
    # Reference count
    refs = IntegerField()
    # Bytes of wired memory used by extension
    size = BigIntegerField()
    # Extension label
    name = TextField()
    # Extension version
    version = TextField()
    # Indexes of extensions this extension is linked against
    linked_against = TextField()
    # Optional path to extension bundle
    path = TextField()

    class Meta:
        table_name = "kernel_extensions"
