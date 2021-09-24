"""
OSQuery docker_container_networks ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class DockerContainerNetworks(BaseModel):
    """
    Docker container networks.
    Examples:
        select * from docker_container_networks
        select * from docker_container_networks where id = '1234567890abcdef'
        select * from docker_container_networks where id = '11b2399e1426d906e62a0c357650e363426d6c56dbe2f35cbaa9b452250e3355'
    """
    # Container ID
    id = TextField()  # {'index': True}
    # Network name
    name = TextField()  # {'index': True}
    # Network ID
    network_id = TextField()
    # Endpoint ID
    endpoint_id = TextField()
    # Gateway
    gateway = TextField()
    # IP address
    ip_address = TextField()
    # IP subnet prefix length
    ip_prefix_len = IntegerField()
    # IPv6 gateway
    ipv6_gateway = TextField()
    # IPv6 address
    ipv6_address = TextField()
    # IPv6 subnet prefix length
    ipv6_prefix_len = IntegerField()
    # MAC address
    mac_address = TextField()

    class Meta:
        table_name = "docker_container_networks"
