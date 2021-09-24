"""
OSQuery user_ssh_keys ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, ForeignKeyField, TextField
from .users import Users


class UserSshKeys(BaseModel):
    """
    Returns the private keys in the users ~/.ssh directory and whether or not they are encrypted.
    Examples:
        select * from users join user_ssh_keys using (uid) where encrypted = 0
    """
    # The local user that owns the key file
    uid = BigIntegerField()  # {'additional': True}
    # Path to key file
    path = TextField()  # {'index': True}
    # 1 if key is encrypted, 0 otherwise
    encrypted = IntegerField()
    user_ssh_keys = ForeignKeyField(Users, backref='uid')

    class Meta:
        table_name = "user_ssh_keys"
