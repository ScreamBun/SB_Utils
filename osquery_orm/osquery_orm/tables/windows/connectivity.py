"""
OSQuery connectivity ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField


class Connectivity(BaseModel):
    """
    Provides the overall system's network state.
    Examples:
        select * from connectivity
        select ipv4_internet from connectivity
    """
    # True if the all interfaces are not connected to any network
    disconnected = IntegerField()
    # True if any interface is connected via IPv4, but has seen no traffic
    ipv4_no_traffic = IntegerField()
    # True if any interface is connected via IPv6, but has seen no traffic
    ipv6_no_traffic = IntegerField()
    # True if any interface is connected to the local subnet via IPv4
    ipv4_subnet = IntegerField()
    # True if any interface is connected to a routed network via IPv4
    ipv4_local_network = IntegerField()
    # True if any interface is connected to the Internet via IPv4
    ipv4_internet = IntegerField()
    # True if any interface is connected to the local subnet via IPv6
    ipv6_subnet = IntegerField()
    # True if any interface is connected to a routed network via IPv6
    ipv6_local_network = IntegerField()
    # True if any interface is connected to the Internet via IPv6
    ipv6_internet = IntegerField()

    class Meta:
        table_name = "connectivity"
