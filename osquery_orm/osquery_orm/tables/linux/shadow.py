"""
OSQuery shadow ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class Shadow(BaseModel):
    """
    Local system users encrypted passwords and related information. Please note, that you usually need superuser rights to access `/etc/shadow`.
    Examples:
        select * from shadow where username = 'root'
    """
    # Password status
    password_status = TextField()
    # Password hashing algorithm
    hash_alg = TextField()
    # Date of last password change (starting from UNIX epoch date)
    last_change = BigIntegerField()
    # Minimal number of days between password changes
    min = BigIntegerField()
    # Maximum number of days between password changes
    max = BigIntegerField()
    # Number of days before password expires to warn user about it
    warning = BigIntegerField()
    # Number of days after password expires until account is blocked
    inactive = BigIntegerField()
    # Number of days since UNIX epoch date until account is disabled
    expire = BigIntegerField()
    # Reserved
    flag = BigIntegerField()
    # Username
    username = TextField()  # {'index': True}

    class Meta:
        table_name = "shadow"
