"""
OSQuery docker_networks ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class DockerNetworks(BaseModel):
    """
    Docker networks information.
    Examples:
        select * from docker_networks
        select * from docker_networks where id = 'cfd2ffd49439'
        select * from docker_networks where id = 'cfd2ffd494395b75d77539761df40cde06a2b6b497e0c9c1adc6c5a79539bfad'
    """
    # Network ID
    id = TextField()  # {'index': True}
    # Network name
    name = TextField()
    # Network driver
    driver = TextField()
    # Time of creation as UNIX time
    created = BigIntegerField()
    # 1 if IPv6 is enabled on this network. 0 otherwise
    enable_ipv6 = IntegerField()
    # Network subnet
    subnet = TextField()
    # Network gateway
    gateway = TextField()

    class Meta:
        table_name = "docker_networks"
