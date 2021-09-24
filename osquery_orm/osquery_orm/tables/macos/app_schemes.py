"""
OSQuery app_schemes ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class AppSchemes(BaseModel):
    """
    OS X application schemes and handlers (e.g., http, file, mailto).
    """
    # Name of the scheme/protocol
    scheme = TextField()
    # Application label for the handler
    handler = TextField()
    # 1 if this handler is the OS default, else 0
    enabled = IntegerField()
    # 1 if this handler does NOT exist on OS X by default, else 0
    external = IntegerField()
    # 1 if this handler is protected (reserved) by OS X, else 0
    protected = IntegerField()

    class Meta:
        table_name = "app_schemes"
