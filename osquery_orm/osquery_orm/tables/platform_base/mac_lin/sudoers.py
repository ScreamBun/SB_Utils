"""
OSQuery sudoers ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Sudoers(BaseModel):
    """
    Rules for running commands as other users via sudo.
    """
    # Source file containing the given rule
    source = TextField()
    # Symbol for given rule
    header = TextField()
    # Rule definition
    rule_details = TextField()

    class Meta:
        table_name = "sudoers"
