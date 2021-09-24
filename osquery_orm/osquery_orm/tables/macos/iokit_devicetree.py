"""
OSQuery iokit_devicetree ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class IokitDevicetree(BaseModel):
    """
    The IOKit registry matching the DeviceTree plane.
    """
    # Device node name
    name = TextField()
    # Best matching device class (most-specific category)
    class_ = TextField(column_name="class")
    # IOKit internal registry ID
    id = BigIntegerField()
    # Parent device registry ID
    parent = BigIntegerField()
    # Device tree path
    device_path = TextField()
    # 1 if the device conforms to IOService else 0
    service = IntegerField()
    # 1 if the device is in a busy state else 0
    busy_state = IntegerField()
    # The device reference count
    retain_count = IntegerField()
    # Device nested depth
    depth = IntegerField()

    class Meta:
        table_name = "iokit_devicetree"
