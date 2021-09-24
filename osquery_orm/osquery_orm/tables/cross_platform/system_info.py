"""
OSQuery system_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class SystemInfo(BaseModel):
    """
    System information for identification.
    """
    # Network hostname including domain
    hostname = TextField()
    # Unique ID provided by the system
    uuid = TextField()
    # CPU type
    cpu_type = TextField()
    # CPU subtype
    cpu_subtype = TextField()
    # CPU brand string, contains vendor and model
    cpu_brand = TextField()
    # Number of physical CPU cores in to the system
    cpu_physical_cores = IntegerField()
    # Number of logical CPU cores available to the system
    cpu_logical_cores = IntegerField()
    # Microcode version
    cpu_microcode = TextField()
    # Total physical memory in bytes
    physical_memory = BigIntegerField()
    # Hardware vendor
    hardware_vendor = TextField()
    # Hardware model
    hardware_model = TextField()
    # Hardware version
    hardware_version = TextField()
    # Device serial number
    hardware_serial = TextField()
    # Board vendor
    board_vendor = TextField()
    # Board model
    board_model = TextField()
    # Board version
    board_version = TextField()
    # Board serial number
    board_serial = TextField()
    # Friendly computer name (optional)
    computer_name = TextField()
    # Local hostname (optional)
    local_hostname = TextField()

    class Meta:
        table_name = "system_info"
