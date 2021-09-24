"""
OSQuery memory_devices ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class MemoryDevices(BaseModel):
    """
    Physical memory device (type 17) information retrieved from SMBIOS.
    """
    # Handle, or instance number, associated with the structure in SMBIOS
    handle = TextField()
    # The memory array that the device is attached to
    array_handle = TextField()
    # Implementation form factor for this memory device
    form_factor = TextField()
    # Total width, in bits, of this memory device, including any check or error-correction bits
    total_width = IntegerField()
    # Data width, in bits, of this memory device
    data_width = IntegerField()
    # Size of memory device in Megabyte
    size = IntegerField()
    # Identifies if memory device is one of a set of devices.  A value of 0 indicates no set affiliation.
    set = IntegerField()
    # String number of the string that identifies the physically-labeled socket or board position where the memory device is located
    device_locator = TextField()
    # String number of the string that identifies the physically-labeled bank where the memory device is located
    bank_locator = TextField()
    # Type of memory used
    memory_type = TextField()
    # Additional details for memory device
    memory_type_details = TextField()
    # Max speed of memory device in megatransfers per second (MT/s)
    max_speed = IntegerField()
    # Configured speed of memory device in megatransfers per second (MT/s)
    configured_clock_speed = IntegerField()
    # Manufacturer ID string
    manufacturer = TextField()
    # Serial number of memory device
    serial_number = TextField()
    # Manufacturer specific asset tag of memory device
    asset_tag = TextField()
    # Manufacturer specific serial number of memory device
    part_number = TextField()
    # Minimum operating voltage of device in millivolts
    min_voltage = IntegerField()
    # Maximum operating voltage of device in millivolts
    max_voltage = IntegerField()
    # Configured operating voltage of device in millivolts
    configured_voltage = IntegerField()

    class Meta:
        table_name = "memory_devices"
