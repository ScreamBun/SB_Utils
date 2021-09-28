"""
OSQuery etc_protocols ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField, IntegerField


class EtcProtocols(BaseModel):
    """
    Line-parsed /etc/protocols.
    """
    name = TextField(help_text="Protocol name")
    number = IntegerField(help_text="Protocol number")
    alias = TextField(help_text="Protocol alias")
    comment = TextField(help_text="Comment with protocol description")

    class Meta:
        table_name = "etc_protocols"
