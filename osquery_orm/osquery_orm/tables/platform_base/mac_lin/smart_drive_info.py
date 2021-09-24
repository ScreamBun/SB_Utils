"""
OSQuery smart_drive_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class SmartDriveInfo(BaseModel):
    """
    Drive information read by SMART controller utilizing autodetect.
    """
    # Name of block device
    device_name = TextField()
    # Physical slot number of device, only exists when hardware storage controller exists
    disk_id = IntegerField()
    # The explicit device type used to retrieve the SMART information
    driver_type = TextField()
    # Drive model family
    model_family = TextField()
    # Device Model
    device_model = TextField()
    # Device serial number
    serial_number = TextField()
    # Device Identifier
    lu_wwn_device_id = TextField()
    # An additional drive identifier if any
    additional_product_id = TextField()
    # Drive firmware version
    firmware_version = TextField()
    # Bytes of drive capacity
    user_capacity = TextField()
    # Bytes of drive sector sizes
    sector_sizes = TextField()
    # Drive RPM
    rotation_rate = TextField()
    # Form factor if reported
    form_factor = TextField()
    # Boolean value for if drive is recognized
    in_smartctl_db = IntegerField()
    # ATA version of drive
    ata_version = TextField()
    # Drive transport type
    transport_type = TextField()
    # SATA version, if any
    sata_version = TextField()
    # Error string for device id read, if any
    read_device_identity_failure = TextField()
    # SMART support status
    smart_supported = TextField()
    # SMART enabled status
    smart_enabled = TextField()
    # Packet device type
    packet_device_type = TextField()
    # Device power mode
    power_mode = TextField()
    # Warning messages from SMART controller
    warnings = TextField()

    class Meta:
        table_name = "smart_drive_info"
