"""
OSQuery managed_policies ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class ManagedPolicies(BaseModel):
    """
    The managed configuration policies from AD, MDM, MCX, etc.
    """
    # System or manager-chosen domain key
    domain = TextField()
    # Optional UUID assigned to policy set
    uuid = TextField()
    # Policy key name
    name = TextField()
    # Policy value
    value = TextField()
    # Policy applies only this user
    username = TextField()
    # 1 if policy was loaded manually, otherwise 0
    manual = IntegerField()

    class Meta:
        table_name = "managed_policies"
