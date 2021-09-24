"""
OSQuery smbios_tables ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class SmbiosTables(BaseModel):
    """
    BIOS (DMI) structure common details and content.
    """
    # Table entry number
    number = IntegerField()
    # Table entry type
    type = IntegerField()
    # Table entry description
    description = TextField()
    # Table entry handle
    handle = IntegerField()
    # Header size in bytes
    header_size = IntegerField()
    # Table entry size in bytes
    size = IntegerField()
    # MD5 hash of table entry
    md5 = TextField()

    class Meta:
        table_name = "smbios_tables"
