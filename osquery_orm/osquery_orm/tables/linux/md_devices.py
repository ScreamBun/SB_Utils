"""
OSQuery md_devices ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class MdDevices(BaseModel):
    """
    Software RAID array settings.
    """
    # md device name
    device_name = TextField()
    # Current state of the array
    status = TextField()
    # Current raid level of the array
    raid_level = IntegerField()
    # size of the array in blocks
    size = BigIntegerField()
    # chunk size in bytes
    chunk_size = BigIntegerField()
    # Number of configured RAID disks in array
    raid_disks = IntegerField()
    # Number of partitions or disk devices to comprise the array
    nr_raid_disks = IntegerField()
    # Number of working disks in array
    working_disks = IntegerField()
    # Number of active disks in array
    active_disks = IntegerField()
    # Number of failed disks in array
    failed_disks = IntegerField()
    # Number of idle disks in array
    spare_disks = IntegerField()
    # State of the superblock
    superblock_state = TextField()
    # Version of the superblock
    superblock_version = TextField()
    # Unix timestamp of last update
    superblock_update_time = BigIntegerField()
    # Pages allocated in in-memory bitmap, if enabled
    bitmap_on_mem = TextField()
    # Bitmap chunk size
    bitmap_chunk_size = TextField()
    # External referenced bitmap file
    bitmap_external_file = TextField()
    # Progress of the recovery activity
    recovery_progress = TextField()
    # Estimated duration of recovery activity
    recovery_finish = TextField()
    # Speed of recovery activity
    recovery_speed = TextField()
    # Progress of the resync activity
    resync_progress = TextField()
    # Estimated duration of resync activity
    resync_finish = TextField()
    # Speed of resync activity
    resync_speed = TextField()
    # Progress of the reshape activity
    reshape_progress = TextField()
    # Estimated duration of reshape activity
    reshape_finish = TextField()
    # Speed of reshape activity
    reshape_speed = TextField()
    # Progress of the check array activity
    check_array_progress = TextField()
    # Estimated duration of the check array activity
    check_array_finish = TextField()
    # Speed of the check array activity
    check_array_speed = TextField()
    # Unused devices
    unused_devices = TextField()
    # Other information associated with array from /proc/mdstat
    other = TextField()

    class Meta:
        table_name = "md_devices"
