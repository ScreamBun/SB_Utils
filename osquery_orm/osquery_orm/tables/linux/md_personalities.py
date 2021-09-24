"""
OSQuery md_personalities ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class MdPersonalities(BaseModel):
    """
    Software RAID setting supported by the kernel.
    """
    # Name of personality supported by kernel
    name = TextField()

    class Meta:
        table_name = "md_personalities"
