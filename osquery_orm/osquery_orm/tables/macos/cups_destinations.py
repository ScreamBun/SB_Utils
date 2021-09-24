"""
OSQuery cups_destinations ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class CupsDestinations(BaseModel):
    """
    Returns all configured printers.
    """
    # Name of the printer
    name = TextField()
    # Option name
    option_name = TextField()
    # Option value
    option_value = TextField()

    class Meta:
        table_name = "cups_destinations"
