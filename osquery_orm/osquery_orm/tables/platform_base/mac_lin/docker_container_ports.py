"""
OSQuery docker_container_ports ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class DockerContainerPorts(BaseModel):
    """
    Docker container ports.
    Examples:
        select * from docker_container_ports
        select * from docker_container_ports where id = '1234567890abcdef'
        select * from docker_container_ports where id = '11b2399e1426d906e62a0c357650e363426d6c56dbe2f35cbaa9b452250e3355'
    """
    # Container ID
    id = TextField()  # {'additional': True}
    # Protocol (tcp, udp)
    type = TextField()
    # Port inside the container
    port = IntegerField()
    # Host IP address on which public port is listening
    host_ip = TextField()
    # Host port
    host_port = IntegerField()

    class Meta:
        table_name = "docker_container_ports"
