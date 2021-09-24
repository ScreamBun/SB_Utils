"""
OSQuery docker_volume_labels ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class DockerVolumeLabels(BaseModel):
    """
    Docker volume labels.
    Examples:
        select * from docker_volume_labels
        select * from docker_volume_labels where name = 'btrfs'
    """
    # Volume name
    name = TextField()  # {'index': True}
    # Label key
    key = TextField()  # {'index': True}
    # Optional label value
    value = TextField()

    class Meta:
        table_name = "docker_volume_labels"
