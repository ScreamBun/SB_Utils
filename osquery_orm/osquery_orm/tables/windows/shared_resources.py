"""
OSQuery shared_resources ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class SharedResources(BaseModel):
    """
    Displays shared resources on a computer system running Windows. This may be a disk drive, printer, interprocess communication, or other sharable device.
    Examples:
        select * from shared_resources
    """
    # A textual description of the object
    description = TextField()
    # Indicates when the object was installed. Lack of a value does not indicate that the object is not installed.
    install_date = TextField()
    # String that indicates the current status of the object.
    status = TextField()
    # Number of concurrent users for this resource has been limited. If True, the value in the MaximumAllowed property is ignored.
    allow_maximum = IntegerField()
    # Limit on the maximum number of users allowed to use this resource concurrently. The value is only valid if the AllowMaximum property is set to FALSE.
    maximum_allowed = IntegerField()
    # Alias given to a path set up as a share on a computer system running Windows.
    name = TextField()
    # Local path of the Windows share.
    path = TextField()
    # Type of resource being shared. Types include: disk drives, print queues, interprocess communications (IPC), and general devices.
    type = IntegerField()

    class Meta:
        table_name = "shared_resources"
