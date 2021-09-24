"""
OSQuery powershell_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, DoubleField, BigIntegerField, TextField


class PowershellEvents(BaseModel):
    """
    Powershell script blocks reconstructed to their full script content, this table requires script block logging to be enabled.
    Examples:
        select * from powershell_events;
        select * from powershell_events where script_text like '%Invoke-Mimikatz%';
        select * from powershell_events where cosine_similarity < 0.25;
    """
    # Timestamp the event was received by the osquery event publisher
    time = BigIntegerField()
    # System time at which the Powershell script event occurred
    datetime = TextField()
    # The unique GUID of the powershell script to which this block belongs
    script_block_id = TextField()
    # The total number of script blocks for this script
    script_block_count = IntegerField()
    # The text content of the Powershell script
    script_text = TextField()
    # The name of the Powershell script
    script_name = TextField()
    # The path for the Powershell script
    script_path = TextField()
    # How similar the Powershell script is to a provided 'normal' character frequency
    cosine_similarity = DoubleField()

    class Meta:
        table_name = "powershell_events"
