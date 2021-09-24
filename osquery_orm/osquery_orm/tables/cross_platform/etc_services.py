"""
OSQuery etc_services ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class EtcServices(BaseModel):
    """
    Line-parsed /etc/services.
    """
    # Service name
    name = TextField()
    # Service port number
    port = IntegerField()
    # Transport protocol (TCP/UDP)
    protocol = TextField()
    # Optional space separated list of other names for a service
    aliases = TextField()
    # Optional comment for a service.
    comment = TextField()

    class Meta:
        table_name = "etc_services"
