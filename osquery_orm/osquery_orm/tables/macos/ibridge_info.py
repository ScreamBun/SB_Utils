"""
OSQuery ibridge_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class IbridgeInfo(BaseModel):
    """
    Information about the Apple iBridge hardware controller.
    """
    # Boot UUID of the iBridge controller
    boot_uuid = TextField()
    # The manufacturer and chip version
    coprocessor_version = TextField()
    # The build version of the firmware
    firmware_version = TextField()
    # Unique id of the iBridge controller
    unique_chip_id = TextField()

    class Meta:
        table_name = "ibridge_info"
