"""
OSQuery docker_container_labels ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class DockerContainerLabels(BaseModel):
    """
    Docker container labels.
    Examples:
        select * from docker_container_labels
        select * from docker_container_labels where id = '1234567890abcdef'
        select * from docker_container_labels where id = '11b2399e1426d906e62a0c357650e363426d6c56dbe2f35cbaa9b452250e3355'
    """
    # Container ID
    id = TextField()  # {'index': True}
    # Label key
    key = TextField()  # {'index': True}
    # Optional label value
    value = TextField()

    class Meta:
        table_name = "docker_container_labels"
