"""
OSQuery docker_version ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class DockerVersion(BaseModel):
    """
    Docker version information.
    Examples:
        select version from docker_version
    """
    # Docker version
    version = TextField()
    # API version
    api_version = TextField()
    # Minimum API version supported
    min_api_version = TextField()
    # Docker build git commit
    git_commit = TextField()
    # Go version
    go_version = TextField()
    # Operating system
    os = TextField()
    # Hardware architecture
    arch = TextField()
    # Kernel version
    kernel_version = TextField()
    # Build time
    build_time = TextField()

    class Meta:
        table_name = "docker_version"
