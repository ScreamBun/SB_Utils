"""
OSQuery ulimit_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class UlimitInfo(BaseModel):
    """
    System resource usage limits.
    Examples:
        select * from ulimit_info
    """
    # System resource to be limited
    type = TextField()
    # Current limit value
    soft_limit = TextField()
    # Maximum limit value
    hard_limit = TextField()

    class Meta:
        table_name = "ulimit_info"
