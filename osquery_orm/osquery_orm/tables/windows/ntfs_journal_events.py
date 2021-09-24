"""
OSQuery ntfs_journal_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class NtfsJournalEvents(BaseModel):
    """
    Track time/action changes to files specified in configuration data.
    """
    # Change action (Write, Delete, etc)
    action = TextField()
    # The category that the event originated from
    category = TextField()
    # Old path (renames only)
    old_path = TextField()
    # Path
    path = TextField()
    # Journal record timestamp
    record_timestamp = TextField()
    # The update sequence number that identifies the journal record
    record_usn = TextField()
    # The ordinal that associates a journal record with a filename
    node_ref_number = TextField()
    # The ordinal that associates a journal record with a filename's parent directory
    parent_ref_number = TextField()
    # The drive letter identifying the source journal
    drive_letter = TextField()
    # File attributes
    file_attributes = TextField()
    # Set to 1 if either path or old_path only contains the file or folder name
    partial = BigIntegerField()
    # Time of file event
    time = BigIntegerField()
    # Event ID
    eid = TextField()  # {'hidden': True}

    class Meta:
        table_name = "ntfs_journal_events"
