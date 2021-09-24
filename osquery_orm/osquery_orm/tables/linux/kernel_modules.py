"""
OSQuery kernel_modules ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class KernelModules(BaseModel):
    """
    Linux kernel modules both loaded and within the load search path.
    """
    # Module name
    name = TextField()
    # Size of module content
    size = BigIntegerField()
    # Module reverse dependencies
    used_by = TextField()
    # Kernel module status
    status = TextField()
    # Kernel module address
    address = TextField()

    class Meta:
        table_name = "kernel_modules"
