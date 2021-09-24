"""
OSQuery elf_dynamic ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class ElfDynamic(BaseModel):
    """
    ELF dynamic section information.
    Examples:
        select * from elf_dynamic where path = '/usr/bin/grep'
    """
    # Tag ID
    tag = IntegerField()
    # Tag value
    value = IntegerField()
    # Class (32 or 64)
    class_ = IntegerField(column_name="class")
    # Path to ELF file
    path = TextField()  # {'required': True, 'index': True}

    class Meta:
        table_name = "elf_dynamic"
