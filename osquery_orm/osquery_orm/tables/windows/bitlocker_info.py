"""
OSQuery bitlocker_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class BitlockerInfo(BaseModel):
    """
    Retrieve bitlocker status of the machine.
    """
    # ID of the encrypted drive.
    device_id = TextField()
    # Drive letter of the encrypted drive.
    drive_letter = TextField()
    # Persistent ID of the drive.
    persistent_volume_id = TextField()
    # The bitlocker conversion status of the drive.
    conversion_status = IntegerField()
    # The bitlocker protection status of the drive.
    protection_status = IntegerField()
    # The encryption type of the device.
    encryption_method = TextField()
    # The FVE metadata version of the drive.
    version = IntegerField()
    # The percentage of the drive that is encrypted.
    percentage_encrypted = IntegerField()
    # The accessibility status of the drive from Windows.
    lock_status = IntegerField()

    class Meta:
        table_name = "bitlocker_info"
