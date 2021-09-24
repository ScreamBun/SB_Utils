"""
OSQuery memory_device_mapped_addresses ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class MemoryDeviceMappedAddresses(BaseModel):
    """
    Data associated for address mapping of physical memory devices.
    """
    # Handle, or instance number, associated with the structure
    handle = TextField()
    # Handle of the memory device structure associated with this structure
    memory_device_handle = TextField()
    # Handle of the memory array mapped address to which this device range is mapped to
    memory_array_mapped_address_handle = TextField()
    # Physical stating address, in kilobytes, of a range of memory mapped to physical memory array
    starting_address = TextField()
    # Physical ending address of last kilobyte of a range of memory mapped to physical memory array
    ending_address = TextField()
    # Identifies the position of the referenced memory device in a row of the address partition
    partition_row_position = IntegerField()
    # The position of the device in a interleave, i.e. 0 indicates non-interleave, 1 indicates 1st interleave, 2 indicates 2nd interleave, etc.
    interleave_position = IntegerField()
    # The max number of consecutive rows from memory device that are accessed in a single interleave transfer; 0 indicates device is non-interleave
    interleave_data_depth = IntegerField()

    class Meta:
        table_name = "memory_device_mapped_addresses"
