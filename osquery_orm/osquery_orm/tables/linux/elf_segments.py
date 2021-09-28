"""
OSQuery elf_segments ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField, IntegerField


class ElfSegments(BaseModel):
    """
    ELF segment information.
    Examples:
        select * from elf_segments where path = '/usr/bin/grep'
    """
    name = TextField(help_text="Segment type/name")
    offset = IntegerField(help_text="Segment offset in file")
    vaddr = IntegerField(help_text="Segment virtual address in memory")
    psize = IntegerField(help_text="Size of segment in file")
    msize = IntegerField(help_text="Segment offset in memory")
    flags = TextField(help_text="Segment attributes")
    align = IntegerField(help_text="Segment alignment")
    path = TextField(help_text="Path to ELF file")  # {'required': True, 'index': True}

    class Meta:
        table_name = "elf_segments"
