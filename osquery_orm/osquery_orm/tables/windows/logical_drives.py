"""
OSQuery logical_drives ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class LogicalDrives(BaseModel):
    """
    Details for logical drives on the system. A logical drive generally represents a single partition.
    Examples:
        select * from logical_drives
        select free_space from logical_drives where device_id = 'C:'
    """
    # The drive id, usually the drive name, e.g., 'C:'.
    device_id = TextField()
    # Deprecated (always 'Unknown').
    type = TextField()
    # The canonical description of the drive, e.g. 'Logical Fixed Disk', 'CD-ROM Disk'.
    description = TextField()
    # The amount of free space, in bytes, of the drive (-1 on failure).
    free_space = BigIntegerField()
    # The total amount of space, in bytes, of the drive (-1 on failure).
    size = BigIntegerField()
    # The file system of the drive.
    file_system = TextField()
    # True if Windows booted from this drive.
    boot_partition = IntegerField()

    class Meta:
        table_name = "logical_drives"
