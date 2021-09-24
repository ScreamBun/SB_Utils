"""
OSQuery memory_array_mapped_addresses ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class MemoryArrayMappedAddresses(BaseModel):
    """
    Data associated for address mapping of physical memory arrays.
    """
    # Handle, or instance number, associated with the structure
    handle = TextField()
    # Handle of the memory array associated with this structure
    memory_array_handle = TextField()
    # Physical stating address, in kilobytes, of a range of memory mapped to physical memory array
    starting_address = TextField()
    # Physical ending address of last kilobyte of a range of memory mapped to physical memory array
    ending_address = TextField()
    # Number of memory devices that form a single row of memory for the address partition of this structure
    partition_width = IntegerField()

    class Meta:
        table_name = "memory_array_mapped_addresses"
