"""
OSQuery elf_segments ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class ElfSegments(BaseModel):
    """
    ELF segment information.
    Examples:
        select * from elf_segments where path = '/usr/bin/grep'
    """
    # Segment type/name
    name = TextField()
    # Segment offset in file
    offset = IntegerField()
    # Segment virtual address in memory
    vaddr = IntegerField()
    # Size of segment in file
    psize = IntegerField()
    # Segment offset in memory
    msize = IntegerField()
    # Segment attributes
    flags = TextField()
    # Segment alignment
    align = IntegerField()
    # Path to ELF file
    path = TextField()  # {'required': True, 'index': True}

    class Meta:
        table_name = "elf_segments"
