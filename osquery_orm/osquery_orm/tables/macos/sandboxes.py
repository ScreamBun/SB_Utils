"""
OSQuery sandboxes ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Sandboxes(BaseModel):
    """
    OS X application sandboxes container details.
    """
    # UTI-format bundle or label ID
    label = TextField()
    # Sandbox owner
    user = TextField()
    # Application sandboxings enabled on container
    enabled = IntegerField()
    # Sandbox-specific identifier
    build_id = TextField()
    # Application bundle used by the sandbox
    bundle_path = TextField()
    # Path to sandbox container directory
    path = TextField()

    class Meta:
        table_name = "sandboxes"
