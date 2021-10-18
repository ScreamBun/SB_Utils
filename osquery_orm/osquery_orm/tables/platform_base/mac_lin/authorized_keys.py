"""
OSQuery authorized_keys ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, ForeignKeyField, IntegerField, TextField
from .users import Users


class AuthorizedKeys(BaseModel):
    """
    A line-delimited authorized_keys table.
    Examples:
        select * from users join authorized_keys using (uid)
    """
    uid = BigIntegerField(help_text="The local owner of authorized_keys file")  # {'additional': True}
    algorithm = TextField(help_text="algorithm of key")
    key = TextField(help_text="parsed authorized keys line")
    key_file = TextField(help_text="Path to the authorized_keys file")
    authorized_keys = ForeignKeyField(Users, backref='uid')

    class Meta:
        table_name = "authorized_keys"


# OS specific properties for Linux
class Linux_AuthorizedKeys(AuthorizedKeys):
    pid_with_namespace = IntegerField(help_text="Pids that contain a namespace")  # {'additional': True, 'hidden': True}
