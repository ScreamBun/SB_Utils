"""
OSQuery memory_error_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class MemoryErrorInfo(BaseModel):
    """
    Data associated with errors of a physical memory array.
    """
    # Handle, or instance number, associated with the structure
    handle = TextField()
    # type of error associated with current error status for array or device
    error_type = TextField()
    # Granularity to which the error can be resolved
    error_granularity = TextField()
    # Memory access operation that caused the error
    error_operation = TextField()
    # Vendor specific ECC syndrome or CRC data associated with the erroneous access
    vendor_syndrome = TextField()
    # 32 bit physical address of the error based on the addressing of the bus to which the memory array is connected
    memory_array_error_address = TextField()
    # 32 bit physical address of the error relative to the start of the failing memory address, in bytes
    device_error_address = TextField()
    # Range, in bytes, within which this error can be determined, when an error address is given
    error_resolution = TextField()

    class Meta:
        table_name = "memory_error_info"
