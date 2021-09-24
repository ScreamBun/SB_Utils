"""
OSQuery time_machine_backups ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class TimeMachineBackups(BaseModel):
    """
    Backups to drives using TimeMachine.
    Examples:
        select alias, backup_date, td.destination_id, root_volume_uuid, encryption from time_machine_backups tb join time_machine_destinations td on (td.destination_id=tb.destination_id);
    """
    # Time Machine destination ID
    destination_id = TextField()
    # Backup Date
    backup_date = IntegerField()

    class Meta:
        table_name = "time_machine_backups"
