"""
OSQuery windows_crashes ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class WindowsCrashes(BaseModel):
    """
    Extracted information from Windows crash logs (Minidumps).
    Examples:
        select * from windows_crashes
        select * from windows_crashes where module like '%electron.exe%'
        select * from windows_crashes where datetime < '2016-10-14'
        select * from windows_crashes where registers like '%rax=0000000000000004%'
        select * from windows_crashes where stack_trace like '%vlc%'
    """
    # Timestamp (log format) of the crash
    datetime = TextField()
    # Path of the crashed module within the process
    module = TextField()
    # Path of the executable file for the crashed process
    path = TextField()
    # Process ID of the crashed process
    pid = BigIntegerField()
    # Thread ID of the crashed thread
    tid = BigIntegerField()
    # File version info of the crashed process
    version = TextField()
    # Uptime of the process in seconds
    process_uptime = BigIntegerField()
    # Multiple stack frames from the stack trace
    stack_trace = TextField()
    # The Windows exception code
    exception_code = TextField()
    # The NTSTATUS error message associated with the exception code
    exception_message = TextField()
    # Address (in hex) where the exception occurred
    exception_address = TextField()
    # The values of the system registers
    registers = TextField()
    # Command-line string passed to the crashed process
    command_line = TextField()
    # Current working directory of the crashed process
    current_directory = TextField()
    # Username of the user who ran the crashed process
    username = TextField()
    # Name of the machine where the crash happened
    machine_name = TextField()
    # Windows major version of the machine
    major_version = IntegerField()
    # Windows minor version of the machine
    minor_version = IntegerField()
    # Windows build number of the crashing machine
    build_number = IntegerField()
    # Type of crash log
    type = TextField()
    # Path of the log file
    crash_path = TextField()

    class Meta:
        table_name = "windows_crashes"
