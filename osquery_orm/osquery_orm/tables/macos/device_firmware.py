"""
OSQuery device_firmware ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class DeviceFirmware(BaseModel):
    """
    A best-effort list of discovered firmware versions.
    """
    # Type of device
    type = TextField()
    # The device name
    device = TextField()  # {'index': True}
    # Firmware version
    version = TextField()

    class Meta:
        table_name = "device_firmware"
