"""
OSQuery process_open_pipes ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class ProcessOpenPipes(BaseModel):
    """
    Pipes and partner processes for each process.
    Examples:
        select * from process_open_pipes
    """
    # Process ID
    pid = BigIntegerField()
    # File descriptor
    fd = BigIntegerField()
    # Pipe open mode (r/w)
    mode = TextField()
    # Pipe inode number
    inode = BigIntegerField()
    # Pipe Type: named vs unnamed/anonymous
    type = TextField()
    # Process ID of partner process sharing a particular pipe
    partner_pid = BigIntegerField()
    # File descriptor of shared pipe at partner's end
    partner_fd = BigIntegerField()
    # Mode of shared pipe at partner's end
    partner_mode = TextField()

    class Meta:
        table_name = "process_open_pipes"
