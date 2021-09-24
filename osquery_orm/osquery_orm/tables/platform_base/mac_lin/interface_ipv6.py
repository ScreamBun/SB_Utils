"""
OSQuery interface_ipv6 ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class InterfaceIpv6(BaseModel):
    """
    IPv6 configuration and stats of network interfaces.
    """
    # Interface name
    interface = TextField()
    # Current Hop Limit
    hop_limit = IntegerField()
    # Enable IP forwarding
    forwarding_enabled = IntegerField()
    # Accept ICMP redirect messages
    redirect_accept = IntegerField()
    # Accept ICMP Router Advertisement
    rtadv_accept = IntegerField()

    class Meta:
        table_name = "interface_ipv6"
