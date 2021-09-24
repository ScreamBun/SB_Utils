"""
OSQuery xprotect_entries ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class XprotectEntries(BaseModel):
    """
    Database of the machine's XProtect signatures.
    """
    # Description of XProtected malware
    name = TextField()
    # Launch services content type
    launch_type = TextField()
    # XProtect identity (SHA1) of content
    identity = TextField()
    # Use this file name to match
    filename = TextField()
    # Use this file type to match
    filetype = TextField()
    # Match any of the identities/patterns for this XProtect name
    optional = IntegerField()
    # Uses a match pattern instead of identity
    uses_pattern = IntegerField()

    class Meta:
        table_name = "xprotect_entries"
