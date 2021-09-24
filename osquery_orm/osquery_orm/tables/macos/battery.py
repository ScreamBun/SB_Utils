"""
OSQuery battery ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Battery(BaseModel):
    """
    Provides information about the internal battery of a Macbook.
    """
    # The battery manufacturer's name
    manufacturer = TextField()
    # The date the battery was manufactured UNIX Epoch
    manufacture_date = IntegerField()
    # The battery's model number
    model = TextField()
    # The battery's unique serial number
    serial_number = TextField()
    # The number of charge/discharge cycles
    cycle_count = IntegerField()
    # One of the following: "Good" describes a well-performing battery, "Fair" describes a functional battery with limited capacity, or "Poor" describes a battery that's not capable of providing power
    health = TextField()
    # One of the following: "Normal" indicates the condition of the battery is within normal tolerances, "Service Needed" indicates that the battery should be checked out by a licensed Mac repair service, "Permanent Failure" indicates the battery needs replacement
    condition = TextField()
    # One of the following: "AC Power" indicates the battery is connected to an external power source, "Battery Power" indicates that the battery is drawing internal power, "Off Line" indicates the battery is off-line or no longer connected
    state = TextField()
    # 1 if the battery is currently being charged by a power source. 0 otherwise
    charging = IntegerField()
    # 1 if the battery is currently completely charged. 0 otherwise
    charged = IntegerField()
    # The battery's designed capacity in mAh
    designed_capacity = IntegerField()
    # The battery's actual capacity when it is fully charged in mAh
    max_capacity = IntegerField()
    # The battery's current charged capacity in mAh
    current_capacity = IntegerField()
    # The percentage of battery remaining before it is drained
    percent_remaining = IntegerField()
    # The battery's current amperage in mA
    amperage = IntegerField()
    # The battery's current voltage in mV
    voltage = IntegerField()
    # The number of minutes until the battery is fully depleted. This value is -1 if this time is still being calculated
    minutes_until_empty = IntegerField()
    # The number of minutes until the battery is fully charged. This value is -1 if this time is still being calculated
    minutes_to_full_charge = IntegerField()

    class Meta:
        table_name = "battery"
