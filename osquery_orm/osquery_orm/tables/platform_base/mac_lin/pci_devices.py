"""
OSQuery pci_devices ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import TextField


class PciDevices(BaseModel):
    """
    PCI devices active on the host system.
    """
    # PCI Device used slot
    pci_slot = TextField()
    # PCI Device class
    pci_class = TextField()
    # PCI Device used driver
    driver = TextField()
    # PCI Device vendor
    vendor = TextField()
    # Hex encoded PCI Device vendor identifier
    vendor_id = TextField()
    # PCI Device model
    model = TextField()
    # Hex encoded PCI Device model identifier
    model_id = TextField()

    class Meta:
        table_name = "pci_devices"


# OS specific properties for Linux
class Linux_PciDevices(PciDevices):
    # PCI Device class ID in hex format
    pci_class_id = TextField()
    # PCI Device  subclass in hex format
    pci_subclass_id = TextField()
    # PCI Device subclass
    pci_subclass = TextField()
    # Vendor ID of PCI device subsystem
    subsystem_vendor_id = TextField()
    # Vendor of PCI device subsystem
    subsystem_vendor = TextField()
    # Model ID of PCI device subsystem
    subsystem_model_id = TextField()
    # Device description of PCI device subsystem
    subsystem_model = TextField()
