"""
OSQuery elf_symbols ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class ElfSymbols(BaseModel):
    """
    ELF symbol list.
    Examples:
        select * from elf_symbols where path = '/usr/bin/grep'
    """
    # Symbol name
    name = TextField()
    # Symbol address (value)
    addr = IntegerField()
    # Size of object
    size = IntegerField()
    # Symbol type
    type = TextField()
    # Binding type
    binding = TextField()
    # Section table index
    offset = IntegerField()
    # Table name containing symbol
    table = TextField()
    # Path to ELF file
    path = TextField()  # {'required': True, 'index': True}

    class Meta:
        table_name = "elf_symbols"
