"""
OSQuery intel_me_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class IntelMeInfo(BaseModel):
    """
    Intel ME/CSE Info.
    """
    # Intel ME version
    version = TextField()

    class Meta:
        table_name = "intel_me_info"
