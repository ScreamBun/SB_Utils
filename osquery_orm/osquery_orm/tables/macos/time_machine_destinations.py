"""
OSQuery time_machine_destinations ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class TimeMachineDestinations(BaseModel):
    """
    Locations backed up to using Time Machine.
    Examples:
        select alias, backup_date, td.destination_id, root_volume_uuid, encryption from time_machine_backups tb join time_machine_destinations td on (td.destination_id=tb.destination_id);
    """
    # Human readable name of drive
    alias = TextField()
    # Time Machine destination ID
    destination_id = TextField()
    # Consistency scan date
    consistency_scan_date = IntegerField()
    # Root UUID of backup volume
    root_volume_uuid = TextField()
    # Bytes available on volume
    bytes_available = IntegerField()
    # Bytes used on volume
    bytes_used = IntegerField()
    # Last known encrypted state
    encryption = TextField()

    class Meta:
        table_name = "time_machine_destinations"
