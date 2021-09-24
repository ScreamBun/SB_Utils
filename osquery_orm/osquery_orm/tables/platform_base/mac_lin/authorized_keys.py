"""
OSQuery authorized_keys ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, ForeignKeyField, TextField
from .users import Users


class AuthorizedKeys(BaseModel):
    """
    A line-delimited authorized_keys table.
    Examples:
        select * from users join authorized_keys using (uid)
    """
    # The local owner of authorized_keys file
    uid = BigIntegerField()  # {'additional': True}
    # algorithm of key
    algorithm = TextField()
    # parsed authorized keys line
    key = TextField()
    # Path to the authorized_keys file
    key_file = TextField()
    authorized_keys = ForeignKeyField(Users, backref='uid')

    class Meta:
        table_name = "authorized_keys"
