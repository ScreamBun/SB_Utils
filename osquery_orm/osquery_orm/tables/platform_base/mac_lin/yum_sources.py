"""
OSQuery yum_sources ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class YumSources(BaseModel):
    """
    Current list of Yum repositories or software channels.
    """
    # Repository name
    name = TextField()
    # Repository base URL
    baseurl = TextField()
    # Whether the repository is used
    enabled = TextField()
    # Whether packages are GPG checked
    gpgcheck = TextField()
    # URL to GPG key
    gpgkey = TextField()

    class Meta:
        table_name = "yum_sources"
