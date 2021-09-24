"""
OSQuery process_open_files ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class ProcessOpenFiles(BaseModel):
    """
    File descriptors for each process.
    Examples:
        select * from process_open_files where pid = 1
    """
    # Process (or thread) ID
    pid = BigIntegerField()  # {'index': True}
    # Process-specific file descriptor number
    fd = BigIntegerField()
    # Filesystem path of descriptor
    path = TextField()

    class Meta:
        table_name = "process_open_files"
