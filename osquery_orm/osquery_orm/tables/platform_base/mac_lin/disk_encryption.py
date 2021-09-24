"""
OSQuery disk_encryption ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, ForeignKeyField, TextField
from .block_devices import BlockDevices


class DiskEncryption(BaseModel):
    """
    Disk encryption status and information.
    """
    # Disk name
    name = TextField()
    # Disk Universally Unique Identifier
    uuid = TextField()
    # 1 If encrypted: true (disk is encrypted), else 0
    encrypted = IntegerField()
    # Description of cipher type and mode if available
    type = TextField()
    # Disk encryption status with one of following values: encrypted | not encrypted | undefined
    encryption_status = TextField()
    disk_encryption = ForeignKeyField(BlockDevices, backref='name')
    disk_encryption = ForeignKeyField(BlockDevices, backref='uuid')

    class Meta:
        table_name = "disk_encryption"


# OS specific properties for MacOS
class MacOS_DiskEncryption(DiskEncryption):
    # Currently authenticated user if available
    uid = TextField()
    # UUID of authenticated user if available
    user_uuid = TextField()
    # FileVault status with one of following values: on | off | unknown
    filevault_status = TextField()
