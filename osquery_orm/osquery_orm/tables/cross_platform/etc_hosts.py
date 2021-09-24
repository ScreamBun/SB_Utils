"""
OSQuery etc_hosts ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class EtcHosts(BaseModel):
    """
    Line-parsed /etc/hosts.
    """
    # IP address mapping
    address = TextField()
    # Raw hosts mapping
    hostnames = TextField()

    class Meta:
        table_name = "etc_hosts"
