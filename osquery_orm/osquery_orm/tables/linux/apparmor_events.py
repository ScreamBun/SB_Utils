"""
OSQuery apparmor_events ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class ApparmorEvents(BaseModel):
    """
    Track AppArmor events.
    """
    # Event type
    type = TextField()
    # Raw audit message
    message = TextField()
    # Time of execution in UNIX time
    time = BigIntegerField()
    # Time of execution in system uptime
    uptime = BigIntegerField()
    # Event ID
    eid = TextField()  # {'hidden': True}
    # Apparmor Status like ALLOWED, DENIED etc.
    apparmor = TextField()
    # Permission requested by the process
    operation = TextField()
    # Parent process PID
    parent = BigIntegerField()
    # Apparmor profile name
    profile = TextField()
    # Process name
    name = TextField()
    # Process ID
    pid = BigIntegerField()
    # Command-line name of the command that was used to invoke the analyzed process
    comm = TextField()
    # Denied permissions for the process
    denied_mask = TextField()
    # Capability requested by the process
    capname = TextField()
    # Filesystem user ID
    fsuid = BigIntegerField()
    # Object owner's user ID
    ouid = BigIntegerField()
    # Capability number
    capability = BigIntegerField()
    # Requested access mask
    requested_mask = TextField()
    # Additional information
    info = TextField()
    # Error information
    error = TextField()
    # AppArmor namespace
    namespace = TextField()
    # AppArmor label
    label = TextField()

    class Meta:
        table_name = "apparmor_events"
