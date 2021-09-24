"""
OSQuery chassis_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class ChassisInfo(BaseModel):
    """
    Display information pertaining to the chassis and its security status.
    Examples:
        select * from chassis_info
    """
    # If TRUE, the frame is equipped with an audible alarm.
    audible_alarm = TextField()
    # If provided, gives a more detailed description of a detected security breach.
    breach_description = TextField()
    # A comma-separated list of chassis types, such as Desktop or Laptop.
    chassis_types = TextField()
    # An extended description of the chassis if available.
    description = TextField()
    # If TRUE, the frame is equipped with a lock.
    lock = TextField()
    # The manufacturer of the chassis.
    manufacturer = TextField()
    # The model of the chassis.
    model = TextField()
    # The physical status of the chassis such as Breach Successful, Breach Attempted, etc.
    security_breach = TextField()
    # The serial number of the chassis.
    serial = TextField()
    # The assigned asset tag number of the chassis.
    smbios_tag = TextField()
    # The Stock Keeping Unit number if available.
    sku = TextField()
    # If available, gives various operational or nonoperational statuses such as OK, Degraded, and Pred Fail.
    status = TextField()
    # If TRUE, the frame is equipped with a visual alarm.
    visible_alarm = TextField()

    class Meta:
        table_name = "chassis_info"
