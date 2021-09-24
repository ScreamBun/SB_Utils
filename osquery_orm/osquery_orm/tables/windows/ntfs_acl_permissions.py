"""
OSQuery ntfs_acl_permissions ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class NtfsAclPermissions(BaseModel):
    """
    Retrieve NTFS ACL permission information for files and directories.
    """
    # Path to the file or directory.
    path = TextField()  # {'required': True, 'index': True}
    # Type of access mode for the access control entry.
    type = TextField()
    # User or group to which the ACE applies.
    principal = TextField()
    # Specific permissions that indicate the rights described by the ACE.
    access = TextField()
    # The inheritance policy of the ACE.
    inherited_from = TextField()

    class Meta:
        table_name = "ntfs_acl_permissions"
