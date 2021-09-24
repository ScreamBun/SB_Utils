"""
OSQuery alf ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Alf(BaseModel):
    """
    OS X application layer firewall (ALF) service details.
    """
    # 1 If allow signed mode is enabled else 0
    allow_signed_enabled = IntegerField()
    # 1 If firewall unloading enabled else 0
    firewall_unload = IntegerField()
    # 1 If the firewall is enabled with exceptions, 2 if the firewall is configured to block all incoming connections, else 0
    global_state = IntegerField()
    # 1 If logging mode is enabled else 0
    logging_enabled = IntegerField()
    # Firewall logging option
    logging_option = IntegerField()
    # 1 If stealth mode is enabled else 0
    stealth_enabled = IntegerField()
    # Application Layer Firewall version
    version = TextField()

    class Meta:
        table_name = "alf"
