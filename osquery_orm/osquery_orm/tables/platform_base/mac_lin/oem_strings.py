"""
OSQuery oem_strings ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class OemStrings(BaseModel):
    """
    OEM defined strings retrieved from SMBIOS.
    """
    # Handle, or instance number, associated with the Type 11 structure
    handle = TextField()
    # The string index of the structure
    number = IntegerField()
    # The value of the OEM string
    value = TextField()

    class Meta:
        table_name = "oem_strings"
