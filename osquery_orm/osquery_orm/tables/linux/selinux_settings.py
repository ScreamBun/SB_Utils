"""
OSQuery selinux_settings ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class SelinuxSettings(BaseModel):
    """
    Track active SELinux settings.
    Examples:
        SELECT * FROM selinux_settings WHERE key = 'enforce'
    """
    # Where the key is located inside the SELinuxFS mount point.
    scope = TextField()
    # Key or class name.
    key = TextField()
    # Active value.
    value = TextField()

    class Meta:
        table_name = "selinux_settings"
