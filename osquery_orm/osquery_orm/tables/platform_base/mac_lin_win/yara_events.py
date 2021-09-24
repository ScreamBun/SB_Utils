"""
OSQuery yara_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class YaraEvents(BaseModel):
    """
    Track YARA matches for files specified in configuration data.
    """
    # The path scanned
    target_path = TextField()
    # The category of the file
    category = TextField()
    # Change action (UPDATE, REMOVE, etc)
    action = TextField()
    # ID used during bulk update
    transaction_id = BigIntegerField()
    # List of YARA matches
    matches = TextField()
    # Number of YARA matches
    count = IntegerField()
    # Matching strings
    strings = TextField()
    # Matching tags
    tags = TextField()
    # Time of the scan
    time = BigIntegerField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "yara_events"
