"""
OSQuery file ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class File(BaseModel):
    """
    Interactive filesystem attributes and metadata.
    Examples:
        select * from file where path = '/etc/passwd'
        select * from file where directory = '/etc/'
        select * from file where path LIKE '/etc/%'
    """
    # Absolute file path
    path = TextField()  # {'required': True, 'index': True}
    # Directory of file(s)
    directory = TextField()  # {'required': True}
    # Name portion of file path
    filename = TextField()
    # Filesystem inode number
    inode = BigIntegerField()
    # Owning user ID
    uid = BigIntegerField()
    # Owning group ID
    gid = BigIntegerField()
    # Permission bits
    mode = TextField()
    # Device ID (optional)
    device = BigIntegerField()
    # Size of file in bytes
    size = BigIntegerField()
    # Block size of filesystem
    block_size = IntegerField()
    # Last access time
    atime = BigIntegerField()
    # Last modification time
    mtime = BigIntegerField()
    # Last status change time
    ctime = BigIntegerField()
    # (B)irth or (cr)eate time
    btime = BigIntegerField()
    # Number of hard links
    hard_links = IntegerField()
    # 1 if the path is a symlink, otherwise 0
    symlink = IntegerField()
    # File status
    type = TextField()

    class Meta:
        table_name = "file"


# OS specific properties for Windows
class Windows_File(File):
    # File attrib string. See: https://ss64.com/nt/attrib.html
    attributes = TextField()
    # Volume serial number
    volume_serial = TextField()
    # file ID
    file_id = TextField()
    # File version
    file_version = TextField()
    # File product version
    product_version = TextField()


# OS specific properties for MacOS
class MacOS_File(File):
    # The BSD file flags (chflags). Possible values: NODUMP, UF_IMMUTABLE, UF_APPEND, OPAQUE, HIDDEN, ARCHIVED, SF_IMMUTABLE, SF_APPEND
    bsd_flags = TextField()


# OS specific properties for Linux
class Linux_File(File):
    # Pids that contain a namespace
    pid_with_namespace = IntegerField()  # {'additional': True, 'hidden': True}
    # Mount namespace id
    mount_namespace_id = TextField()  # {'hidden': True}
