"""
OSQuery memory_arrays ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class MemoryArrays(BaseModel):
    """
    Data associated with collection of memory devices that operate to form a memory address.
    """
    # Handle, or instance number, associated with the array
    handle = TextField()
    # Physical location of the memory array
    location = TextField()
    # Function for which the array is used
    use = TextField()
    # Primary hardware error correction or detection method supported
    memory_error_correction = TextField()
    # Maximum capacity of array in gigabytes
    max_capacity = IntegerField()
    # Handle, or instance number, associated with any error that was detected for the array
    memory_error_info_handle = TextField()
    # Number of memory devices on array
    number_memory_devices = IntegerField()

    class Meta:
        table_name = "memory_arrays"
