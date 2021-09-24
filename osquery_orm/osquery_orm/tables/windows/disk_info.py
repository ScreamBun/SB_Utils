"""
OSQuery disk_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class DiskInfo(BaseModel):
    """
    Retrieve basic information about the physical disks of a system.
    """
    # Number of detected partitions on disk.
    partitions = IntegerField()
    # Physical drive number of the disk.
    disk_index = IntegerField()
    # The interface type of the disk.
    type = TextField()
    # The unique identifier of the drive on the system.
    id = TextField()
    # The unique identifier of the drive on the system.
    pnp_device_id = TextField()
    # Size of the disk.
    disk_size = BigIntegerField()
    # The manufacturer of the disk.
    manufacturer = TextField()
    # Hard drive model.
    hardware_model = TextField()
    # The label of the disk object.
    name = TextField()
    # The serial number of the disk.
    serial = TextField()
    # The OS's description of the disk.
    description = TextField()

    class Meta:
        table_name = "disk_info"
