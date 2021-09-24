"""
OSQuery ycloud_instance_metadata ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class YcloudInstanceMetadata(BaseModel):
    """
    Yandex.Cloud instance metadata.
    Examples:
        select * from ycloud_instance_metadata
        select * from ycloud_instance_metadata where metadata_endpoint="http://169.254.169.254"
    """
    # Unique identifier for the VM
    instance_id = TextField()  # {'index': True}
    # Folder identifier for the VM
    folder_id = TextField()
    # Name of the VM
    name = TextField()
    # Description of the VM
    description = TextField()
    # Hostname of the VM
    hostname = TextField()
    # Availability zone of the VM
    zone = TextField()
    # SSH public key. Only available if supplied at instance launch time
    ssh_public_key = TextField()
    # Indicates if serial port is enabled for the VM
    serial_port_enabled = TextField()
    # Endpoint used to fetch VM metadata
    metadata_endpoint = TextField()  # {'index': True}

    class Meta:
        table_name = "ycloud_instance_metadata"
