"""
OSQuery kernel_panics ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class KernelPanics(BaseModel):
    """
    System kernel panic logs.
    """
    # Location of log file
    path = TextField()
    # Formatted time of the event
    time = TextField()
    # A space delimited line of register:value pairs
    registers = TextField()
    # Backtrace of the crashed module
    frame_backtrace = TextField()
    # Modules appearing in the crashed module's backtrace
    module_backtrace = TextField()
    # Module dependencies existing in crashed module's backtrace
    dependencies = TextField()
    # Process name corresponding to crashed thread
    name = TextField()
    # Version of the operating system
    os_version = TextField()
    # Version of the system kernel
    kernel_version = TextField()
    # Physical system model, for example 'MacBookPro12,1 (Mac-E43C1C25D4880AD6)'
    system_model = TextField()
    # System uptime at kernel panic in nanoseconds
    uptime = BigIntegerField()
    # Last loaded module before panic
    last_loaded = TextField()
    # Last unloaded module before panic
    last_unloaded = TextField()

    class Meta:
        table_name = "kernel_panics"
