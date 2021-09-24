"""
OSQuery safari_extensions ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, ForeignKeyField, TextField
from ..cross_platform import MacOS_Users


class SafariExtensions(BaseModel):
    """
    Safari browser extension details for all users.
    Examples:
        select count(*) from users JOIN safari_extensions using (uid)
    """
    # The local user that owns the extension
    uid = BigIntegerField()  # {'index': True}
    # Extension display name
    name = TextField()
    # Extension identifier
    identifier = TextField()
    # Extension long version
    version = TextField()
    # Bundle SDK used to compile extension
    sdk = TextField()
    # Extension-supplied update URI
    update_url = TextField()
    # Optional extension author
    author = TextField()
    # Optional developer identifier
    developer_id = TextField()
    # Optional extension description text
    description = TextField()
    # Path to extension XAR bundle
    path = TextField()
    safari_extensions = ForeignKeyField(MacOS_Users, backref='uid')

    class Meta:
        table_name = "safari_extensions"
