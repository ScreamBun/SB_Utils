"""
OSQuery hash ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Hash(BaseModel):
    """
    Filesystem hash data.
    Examples:
        select * from hash where path = '/etc/passwd'
        select * from hash where directory = '/etc/'
    """
    # Must provide a path or directory
    path = TextField()  # {'index': True, 'required': True}
    # Must provide a path or directory
    directory = TextField()  # {'required': True}
    # MD5 hash of provided filesystem data
    md5 = TextField()
    # SHA1 hash of provided filesystem data
    sha1 = TextField()
    # SHA256 hash of provided filesystem data
    sha256 = TextField()

    class Meta:
        table_name = "hash"


# OS specific properties for Posix
class Posix_Hash(Hash):
    # ssdeep hash of provided filesystem data
    ssdeep = TextField()


# OS specific properties for Linux
class Linux_Hash(Hash):
    # Pids that contain a namespace
    pid_with_namespace = IntegerField()  # {'additional': True, 'hidden': True}
    # Mount namespace id
    mount_namespace_id = TextField()  # {'hidden': True}
