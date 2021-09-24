"""
OSQuery apt_sources ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class AptSources(BaseModel):
    """
    Current list of APT repositories or software channels.
    """
    # Repository name
    name = TextField()
    # Source file
    source = TextField()
    # Repository base URI
    base_uri = TextField()
    # Release name
    release = TextField()
    # Repository source version
    version = TextField()
    # Repository maintainer
    maintainer = TextField()
    # Repository components
    components = TextField()
    # Repository architectures
    architectures = TextField()

    class Meta:
        table_name = "apt_sources"
