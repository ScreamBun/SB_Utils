"""
OSQuery elf_sections ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class ElfSections(BaseModel):
    """
    ELF section information.
    Examples:
        select * from elf_sections where path = '/usr/bin/grep'
    """
    # Section name
    name = TextField()
    # Section type
    type = IntegerField()
    # Section virtual address in memory
    vaddr = IntegerField()
    # Offset of section in file
    offset = IntegerField()
    # Size of section
    size = IntegerField()
    # Section attributes
    flags = TextField()
    # Link to other section
    link = TextField()
    # Segment alignment
    align = IntegerField()
    # Path to ELF file
    path = TextField()  # {'required': True, 'index': True}

    class Meta:
        table_name = "elf_sections"
