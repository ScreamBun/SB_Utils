"""
OSQuery package_bom ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class PackageBom(BaseModel):
    """
    OS X package bill of materials (BOM) file list.
    Examples:
        select * from package_bom where path = '/var/db/receipts/com.apple.pkg.MobileDevice.bom'
    """
    # Package file or directory
    filepath = TextField()
    # Expected user of file or directory
    uid = IntegerField()
    # Expected group of file or directory
    gid = IntegerField()
    # Expected permissions
    mode = IntegerField()
    # Expected file size
    size = BigIntegerField()
    # Timestamp the file was installed
    modified_time = IntegerField()
    # Path of package bom
    path = TextField()  # {'required': True}

    class Meta:
        table_name = "package_bom"
