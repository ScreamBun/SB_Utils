"""
OSQuery lxd_networks ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class LxdNetworks(BaseModel):
    """
    LXD network information.
    Examples:
        select * from lxd_networks
    """
    # Name of the network
    name = TextField()
    # Type of network
    type = TextField()
    # 1 if network created by LXD, 0 otherwise
    managed = IntegerField()
    # IPv4 address
    ipv4_address = TextField()
    # IPv6 address
    ipv6_address = TextField()
    # URLs for containers using this network
    used_by = TextField()
    # Number of bytes received on this network
    bytes_received = BigIntegerField()
    # Number of bytes sent on this network
    bytes_sent = BigIntegerField()
    # Number of packets received on this network
    packets_received = BigIntegerField()
    # Number of packets sent on this network
    packets_sent = BigIntegerField()
    # Hardware address for this network
    hwaddr = TextField()
    # Network status
    state = TextField()
    # MTU size
    mtu = IntegerField()

    class Meta:
        table_name = "lxd_networks"
