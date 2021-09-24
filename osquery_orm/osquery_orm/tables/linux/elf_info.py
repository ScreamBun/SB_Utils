"""
OSQuery elf_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class ElfInfo(BaseModel):
    """
    ELF file information.
    Examples:
        select * from elf_info where path = '/usr/bin/grep'
    """
    # Class type, 32 or 64bit
    class_ = TextField(column_name="class")
    # Section type
    abi = TextField()
    # Section virtual address in memory
    abi_version = IntegerField()
    # Offset of section in file
    type = TextField()
    # Machine type
    machine = IntegerField()
    # Object file version
    version = IntegerField()
    # Entry point address
    entry = BigIntegerField()
    # ELF header flags
    flags = IntegerField()
    # Path to ELF file
    path = TextField()  # {'required': True, 'index': True}

    class Meta:
        table_name = "elf_info"
