"""
OSQuery acpi_tables ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class AcpiTables(BaseModel):
    """
    Firmware ACPI functional table common metadata and content.
    """
    # ACPI table name
    name = TextField()
    # Size of compiled table data
    size = IntegerField()
    # MD5 hash of table content
    md5 = TextField()

    class Meta:
        table_name = "acpi_tables"
