"""
OSQuery usb_devices ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class UsbDevices(BaseModel):
    """
    USB devices that are actively plugged into the host system.
    """
    # USB Device used address
    usb_address = IntegerField()
    # USB Device used port
    usb_port = IntegerField()
    # USB Device vendor string
    vendor = TextField()
    # Hex encoded USB Device vendor identifier
    vendor_id = TextField()
    # USB Device version number
    version = TextField()
    # USB Device model string
    model = TextField()
    # Hex encoded USB Device model identifier
    model_id = TextField()
    # USB Device serial connection
    serial = TextField()
    # USB Device class
    class_ = TextField(column_name="class")
    # USB Device subclass
    subclass = TextField()
    # USB Device protocol
    protocol = TextField()
    # 1 If USB device is removable else 0
    removable = IntegerField()

    class Meta:
        table_name = "usb_devices"
