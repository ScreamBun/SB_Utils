"""
OSQuery load_average ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class LoadAverage(BaseModel):
    """
    Displays information about the system wide load averages.
    Examples:
        select * from load_average;
    """
    # Period over which the average is calculated.
    period = TextField()
    # Load average over the specified period.
    average = TextField()

    class Meta:
        table_name = "load_average"
