"""
OSQuery etc_hosts ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class EtcHosts(BaseModel):
    """
    Line-parsed /etc/hosts.
    """
    address = TextField(help_text="IP address mapping")
    hostnames = TextField(help_text="Raw hosts mapping")

    class Meta:
        table_name = "etc_hosts"
