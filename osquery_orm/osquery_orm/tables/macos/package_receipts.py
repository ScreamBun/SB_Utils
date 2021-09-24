"""
OSQuery package_receipts ORM
"""
from osquery_orm.orm import BaseModel
from peewee import DoubleField, TextField


class PackageReceipts(BaseModel):
    """
    OS X package receipt details.
    Examples:
        select * from package_bom where path = '/var/db/receipts/com.apple.pkg.MobileDevice.bom'
    """
    # Package domain identifier
    package_id = TextField()
    # Filename of original .pkg file
    package_filename = TextField()  # {'index': True, 'hidden': True}
    # Installed package version
    version = TextField()
    # Optional relative install path on volume
    location = TextField()
    # Timestamp of install time
    install_time = DoubleField()
    # Name of installer process
    installer_name = TextField()
    # Path of receipt plist
    path = TextField()  # {'additional': True}

    class Meta:
        table_name = "package_receipts"
