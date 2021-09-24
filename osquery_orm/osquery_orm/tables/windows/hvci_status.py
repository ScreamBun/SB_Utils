"""
OSQuery hvci_status ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class HvciStatus(BaseModel):
    """
    Retrieve HVCI info of the machine.
    """
    # The version number of the Device Guard build.
    version = TextField()
    # The instance ID of Device Guard.
    instance_identifier = TextField()
    # The status of the virtualization based security settings. Returns UNKNOWN if an error is encountered.
    vbs_status = TextField()
    # The status of the code integrity policy enforcement settings. Returns UNKNOWN if an error is encountered.
    code_integrity_policy_enforcement_status = TextField()
    # The status of the User Mode Code Integrity security settings. Returns UNKNOWN if an error is encountered.
    umci_policy_status = TextField()

    class Meta:
        table_name = "hvci_status"
