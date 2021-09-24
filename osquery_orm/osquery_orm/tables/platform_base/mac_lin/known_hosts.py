"""
OSQuery known_hosts ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, ForeignKeyField, TextField
from .users import Users


class KnownHosts(BaseModel):
    """
    A line-delimited known_hosts table.
    Examples:
        select * from users join known_hosts using (uid)
    """
    # The local user that owns the known_hosts file
    uid = BigIntegerField()  # {'index': True}
    # parsed authorized keys line
    key = TextField()
    # Path to known_hosts file
    key_file = TextField()
    known_hosts = ForeignKeyField(Users, backref='uid')

    class Meta:
        table_name = "known_hosts"
