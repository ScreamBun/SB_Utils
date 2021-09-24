"""
OSQuery smc_keys ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class SmcKeys(BaseModel):
    """
    Apple's system management controller keys.
    Examples:
        select * from smc_keys where key = 'MOJO'
    """
    # 4-character key
    key = TextField()  # {'additional': True, 'index': True}
    # SMC-reported type literal type
    type = TextField()
    # Reported size of data in bytes
    size = IntegerField()
    # A type-encoded representation of the key value
    value = TextField()
    # 1 if this key is normally hidden, otherwise 0
    hidden = IntegerField()

    class Meta:
        table_name = "smc_keys"
