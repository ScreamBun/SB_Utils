"""
OSQuery iokit_registry ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class IokitRegistry(BaseModel):
    """
    The full IOKit registry without selecting a plane.
    """
    # Default name of the node
    name = TextField()
    # Best matching device class (most-specific category)
    class_ = TextField(column_name="class")
    # IOKit internal registry ID
    id = BigIntegerField()
    # Parent registry ID
    parent = BigIntegerField()
    # 1 if the node is in a busy state else 0
    busy_state = IntegerField()
    # The node reference count
    retain_count = IntegerField()
    # Node nested depth
    depth = IntegerField()

    class Meta:
        table_name = "iokit_registry"
