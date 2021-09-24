"""
OSQuery logon_sessions ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class LogonSessions(BaseModel):
    """
    Windows Logon Session.
    Examples:
        select * from logon_sessions;
    """
    # A locally unique identifier (LUID) that identifies a logon session.
    logon_id = IntegerField()
    # The account name of the security principal that owns the logon session.
    user = TextField()
    # The name of the domain used to authenticate the owner of the logon session.
    logon_domain = TextField()
    # The authentication package used to authenticate the owner of the logon session.
    authentication_package = TextField()
    # The logon method.
    logon_type = TextField()
    # The Terminal Services session identifier.
    session_id = IntegerField()
    # The user's security identifier (SID).
    logon_sid = TextField()
    # The time the session owner logged on.
    logon_time = BigIntegerField()
    # The name of the server used to authenticate the owner of the logon session.
    logon_server = TextField()
    # The DNS name for the owner of the logon session.
    dns_domain_name = TextField()
    # The user principal name (UPN) for the owner of the logon session.
    upn = TextField()
    # The script used for logging on.
    logon_script = TextField()
    # The home directory for the logon session.
    profile_path = TextField()
    # The home directory for the logon session.
    home_directory = TextField()
    # The drive location of the home directory of the logon session.
    home_directory_drive = TextField()

    class Meta:
        table_name = "logon_sessions"
