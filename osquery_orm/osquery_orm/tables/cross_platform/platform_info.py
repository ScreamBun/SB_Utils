"""
OSQuery platform_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class PlatformInfo(BaseModel):
    """
    Information about EFI/UEFI/ROM and platform/boot.
    """
    # Platform code vendor
    vendor = TextField()
    # Platform code version
    version = TextField()
    # Self-reported platform code update date
    date = TextField()
    # BIOS major and minor revision
    revision = TextField()
    # Relative address of firmware mapping
    address = TextField()
    # Size in bytes of firmware
    size = TextField()
    # (Optional) size of firmware volume
    volume_size = IntegerField()
    # Platform-specific additional information
    extra = TextField()

    class Meta:
        table_name = "platform_info"
