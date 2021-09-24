"""
OSQuery disk_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class DiskEvents(BaseModel):
    """
    Track DMG disk image events (appearance/disappearance) when opened.
    """
    # Appear or disappear
    action = TextField()
    # Path of the DMG file accessed
    path = TextField()
    # Disk event name
    name = TextField()
    # Disk event BSD name
    device = TextField()  # {'aliases': ['bsd_name']}
    # UUID of the volume inside DMG if available
    uuid = TextField()
    # Size of partition in bytes
    size = BigIntegerField()
    # 1 if ejectable, 0 if not
    ejectable = IntegerField()
    # 1 if mountable, 0 if not
    mountable = IntegerField()
    # 1 if writable, 0 if not
    writable = IntegerField()
    # Disk event content
    content = TextField()
    # Disk event media name string
    media_name = TextField()
    # Disk event vendor string
    vendor = TextField()
    # Filesystem if available
    filesystem = TextField()
    # UDIF Master checksum if available (CRC32)
    checksum = TextField()
    # Time of appearance/disappearance in UNIX time
    time = BigIntegerField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "disk_events"
