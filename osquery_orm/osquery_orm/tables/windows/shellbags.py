"""
OSQuery shellbags ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Shellbags(BaseModel):
    """
    Shows directories accessed via Windows Explorer.
    Examples:
        select * from shellbags;
    """
    # User SID
    sid = TextField()
    # Shellbags source Registry file
    source = TextField()
    # Directory name.
    path = TextField()
    # Directory Modified time.
    modified_time = BigIntegerField()
    # Directory Created time.
    created_time = BigIntegerField()
    # Directory Accessed time.
    accessed_time = BigIntegerField()
    # Directory master file table entry.
    mft_entry = BigIntegerField()
    # Directory master file table sequence.
    mft_sequence = IntegerField()

    class Meta:
        table_name = "shellbags"
