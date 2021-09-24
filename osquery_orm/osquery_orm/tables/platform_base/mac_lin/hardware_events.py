"""
OSQuery hardware_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class HardwareEvents(BaseModel):
    """
    Hardware (PCI/USB/HID) events from UDEV or IOKit.
    """
    # Remove, insert, change properties, etc
    action = TextField()
    # Local device path assigned (optional)
    path = TextField()
    # Type of hardware and hardware event
    type = TextField()
    # Driver claiming the device
    driver = TextField()
    # Hardware device vendor
    vendor = TextField()
    # Hex encoded Hardware vendor identifier
    vendor_id = TextField()
    # Hardware device model
    model = TextField()
    # Hex encoded Hardware model identifier
    model_id = TextField()
    # Device serial (optional)
    serial = TextField()
    # Device revision (optional)
    revision = TextField()
    # Time of hardware event
    time = BigIntegerField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "hardware_events"
