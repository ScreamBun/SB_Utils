"""
OSQuery temperature_sensors ORM
"""
from osquery_orm.orm import BaseModel
from peewee import DoubleField, ForeignKeyField, TextField
from .smc_keys import SmcKeys


class TemperatureSensors(BaseModel):
    """
    Machine's temperature sensors.
    """
    # The SMC key on OS X
    key = TextField()  # {'index': True}
    # Name of temperature source
    name = TextField()
    # Temperature in Celsius
    celsius = DoubleField()
    # Temperature in Fahrenheit
    fahrenheit = DoubleField()
    temperature_sensors = ForeignKeyField(SmcKeys, backref='key')

    class Meta:
        table_name = "temperature_sensors"
