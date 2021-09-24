"""
OSQuery augeas ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Augeas(BaseModel):
    """
    Configuration files parsed by augeas.
    Examples:
        select * from augeas where path = '/etc/hosts'
    """
    # The node path of the configuration item
    node = TextField()  # {'index': True}
    # The value of the configuration item
    value = TextField()
    # The label of the configuration item
    label = TextField()
    # The path to the configuration file
    path = TextField()  # {'additional': True}

    class Meta:
        table_name = "augeas"
