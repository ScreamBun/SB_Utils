"""
OSQuery appcompat_shims ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class AppcompatShims(BaseModel):
    """
    Application Compatibility shims are a way to persist malware. This table presents the AppCompat Shim information from the registry in a nice format. See http://files.brucon.org/2015/Tomczak_and_Ballenthin_Shims_for_the_Win.pdf for more details.
    Examples:
        select * from appcompat_shims;
    """
    # Name of the executable that is being shimmed. This is pulled from the registry.
    executable = TextField()
    # This is the path to the SDB database.
    path = TextField()
    # Description of the SDB.
    description = TextField()
    # Install time of the SDB
    install_time = IntegerField()
    # Type of the SDB database.
    type = TextField()
    # Unique GUID of the SDB.
    sdb_id = TextField()

    class Meta:
        table_name = "appcompat_shims"
