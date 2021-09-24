"""
OSQuery process_memory_map ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class ProcessMemoryMap(BaseModel):
    """
    Process memory mapped files and pseudo device/regions.
    Examples:
        select * from process_memory_map where pid = 1
    """
    # Process (or thread) ID
    pid = IntegerField()  # {'index': True}
    # Virtual start address (hex)
    start = TextField()
    # Virtual end address (hex)
    end = TextField()
    # r=read, w=write, x=execute, p=private (cow)
    permissions = TextField()
    # Offset into mapped path
    offset = BigIntegerField()
    # MA:MI Major/minor device ID
    device = TextField()
    # Mapped path inode, 0 means uninitialized (BSS)
    inode = IntegerField()
    # Path to mapped file or mapped type
    path = TextField()
    # 1 If path is a pseudo path, else 0
    pseudo = IntegerField()

    class Meta:
        table_name = "process_memory_map"
