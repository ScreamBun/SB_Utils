"""
OSQuery etc_protocols ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class EtcProtocols(BaseModel):
    """
    Line-parsed /etc/protocols.
    """
    # Protocol name
    name = TextField()
    # Protocol number
    number = IntegerField()
    # Protocol alias
    alias = TextField()
    # Comment with protocol description
    comment = TextField()

    class Meta:
        table_name = "etc_protocols"
