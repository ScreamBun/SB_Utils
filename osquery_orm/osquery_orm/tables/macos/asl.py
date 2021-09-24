"""
OSQuery asl ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Asl(BaseModel):
    """
    Queries the Apple System Log data structure for system events.
    """
    # Unix timestamp.  Set automatically
    time = IntegerField()  # {'additional': True}
    # Nanosecond time.
    time_nano_sec = IntegerField()  # {'additional': True}
    # Sender's address (set by the server).
    host = TextField()  # {'additional': True}
    # Sender's identification string.  Default is process name.
    sender = TextField()  # {'additional': True}
    # Sender's facility.  Default is 'user'.
    facility = TextField()  # {'additional': True}
    # Sending process ID encoded as a string.  Set automatically.
    pid = IntegerField()  # {'additional': True}
    # GID that sent the log message (set by the server).
    gid = BigIntegerField()  # {'additional': True}
    # UID that sent the log message (set by the server).
    uid = BigIntegerField()  # {'additional': True}
    # Log level number.  See levels in asl.h.
    level = IntegerField()  # {'additional': True}
    # Message text.
    message = TextField()  # {'additional': True}
    # Reference PID for messages proxied by launchd
    ref_pid = IntegerField()  # {'additional': True}
    # Reference process for messages proxied by launchd
    ref_proc = TextField()  # {'additional': True}
    # Extra columns, in JSON format. Queries against this column are performed entirely in SQLite, so do not benefit from efficient querying via asl.h.
    extra = TextField()

    class Meta:
        table_name = "asl"
