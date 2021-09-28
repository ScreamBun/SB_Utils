"""
OSQuery apt_sources ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField, IntegerField


class AptSources(BaseModel):
    """
    Current list of APT repositories or software channels.
    """
    name = TextField(help_text="Repository name")
    source = TextField(help_text="Source file")
    base_uri = TextField(help_text="Repository base URI")
    release = TextField(help_text="Release name")
    version = TextField(help_text="Repository source version")
    maintainer = TextField(help_text="Repository maintainer")
    components = TextField(help_text="Repository components")
    architectures = TextField(help_text="Repository architectures")

    class Meta:
        table_name = "apt_sources"


# OS specific properties for Linux
class Linux_AptSources(AptSources):
    pid_with_namespace = IntegerField(help_text="Pids that contain a namespace")  # {'additional': True, 'hidden': True}
