"""
OSQuery kernel_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class KernelInfo(BaseModel):
    """
    Basic active kernel information.
    """
    # Kernel version
    version = TextField()
    # Kernel arguments
    arguments = TextField()
    # Kernel path
    path = TextField()
    # Kernel device identifier
    device = TextField()

    class Meta:
        table_name = "kernel_info"
