"""
OSQuery azure_instance_metadata ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class AzureInstanceMetadata(BaseModel):
    """
    Azure instance metadata.
    Examples:
        select * from ec2_instance_metadata
    """
    # Azure Region the VM is running in
    location = TextField()
    # Name of the VM
    name = TextField()
    # Offer information for the VM image (Azure image gallery VMs only)
    offer = TextField()
    # Publisher of the VM image
    publisher = TextField()
    # SKU for the VM image
    sku = TextField()
    # Version of the VM image
    version = TextField()
    # Linux or Windows
    os_type = TextField()
    # Update domain the VM is running in
    platform_update_domain = TextField()
    # Fault domain the VM is running in
    platform_fault_domain = TextField()
    # Unique identifier for the VM
    vm_id = TextField()  # {'index': True}
    # VM size
    vm_size = TextField()
    # Azure subscription for the VM
    subscription_id = TextField()
    # Resource group for the VM
    resource_group_name = TextField()
    # Placement group for the VM scale set
    placement_group_id = TextField()
    # VM scale set name
    vm_scale_set_name = TextField()
    # Availability zone of the VM
    zone = TextField()

    class Meta:
        table_name = "azure_instance_metadata"
