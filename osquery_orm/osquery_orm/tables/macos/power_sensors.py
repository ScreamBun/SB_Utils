"""
OSQuery power_sensors ORM
"""
from osquery_orm.orm import BaseModel
from peewee import ForeignKeyField, TextField
from .smc_keys import SmcKeys


class PowerSensors(BaseModel):
    """
    Machine power (currents, voltages, wattages, etc) sensors.
    Examples:
        select * from power_sensors where category = 'voltage'
    """
    # The SMC key on OS X
    key = TextField()  # {'index': True}
    # The sensor category: currents, voltage, wattage
    category = TextField()
    # Name of power source
    name = TextField()
    # Power in Watts
    value = TextField()
    power_sensors = ForeignKeyField(SmcKeys, backref='key')

    class Meta:
        table_name = "power_sensors"
