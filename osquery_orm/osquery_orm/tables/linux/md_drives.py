"""
OSQuery md_drives ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class MdDrives(BaseModel):
    """
    Drive devices used for Software RAID.
    """
    # md device name
    md_device_name = TextField()
    # Drive device name
    drive_name = TextField()
    # Slot position of disk
    slot = IntegerField()
    # State of the drive
    state = TextField()

    class Meta:
        table_name = "md_drives"
