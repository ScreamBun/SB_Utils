"""
OSQuery drivers ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Drivers(BaseModel):
    """
    Details for in-use Windows device drivers. This does not display installed but unused drivers.
    Examples:
        select * from drivers
    """
    # Device ID
    device_id = TextField()
    # Device name
    device_name = TextField()
    # Path to driver image file
    image = TextField()
    # Driver description
    description = TextField()
    # Driver service name, if one exists
    service = TextField()
    # Driver service registry key
    service_key = TextField()
    # Driver version
    version = TextField()
    # Associated inf file
    inf = TextField()
    # Device/driver class name
    class_ = TextField(column_name="class")
    # Driver provider
    provider = TextField()
    # Device manufacturer
    manufacturer = TextField()
    # Driver key
    driver_key = TextField()
    # Driver date
    date = BigIntegerField()
    # Whether the driver is signed or not
    signed = IntegerField()

    class Meta:
        table_name = "drivers"
