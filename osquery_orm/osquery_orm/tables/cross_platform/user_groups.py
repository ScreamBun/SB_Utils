"""
OSQuery user_groups ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField


class UserGroups(BaseModel):
    """
    Local system user group relationships.
    """
    # User ID
    uid = BigIntegerField()  # {'index': True}
    # Group ID
    gid = BigIntegerField()  # {'index': True}

    class Meta:
        table_name = "user_groups"
