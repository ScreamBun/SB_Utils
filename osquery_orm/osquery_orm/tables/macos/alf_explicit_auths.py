"""
OSQuery alf_explicit_auths ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class AlfExplicitAuths(BaseModel):
    """
    ALF services explicitly allowed to perform networking.
    """
    # Process name explicitly allowed
    process = TextField()

    class Meta:
        table_name = "alf_explicit_auths"
