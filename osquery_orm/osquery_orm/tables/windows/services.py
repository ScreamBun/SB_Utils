"""
OSQuery services ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Services(BaseModel):
    """
    Lists all installed Windows services and their relevant data.
    Examples:
        select * from services
    """
    # Service name
    name = TextField()
    # Service Type: OWN_PROCESS, SHARE_PROCESS and maybe Interactive (can interact with the desktop)
    service_type = TextField()
    # Service Display name
    display_name = TextField()
    # Service Current status: STOPPED, START_PENDING, STOP_PENDING, RUNNING, CONTINUE_PENDING, PAUSE_PENDING, PAUSED
    status = TextField()
    # the Process ID of the service
    pid = IntegerField()
    # Service start type: BOOT_START, SYSTEM_START, AUTO_START, DEMAND_START, DISABLED
    start_type = TextField()
    # The error code that the service uses to report an error that occurs when it is starting or stopping
    win32_exit_code = IntegerField()
    # The service-specific error code that the service returns when an error occurs while the service is starting or stopping
    service_exit_code = IntegerField()
    # Path to Service Executable
    path = TextField()
    # Path to ServiceDll
    module_path = TextField()
    # Service Description
    description = TextField()
    # The name of the account that the service process will be logged on as when it runs. This name can be of the form Domain\UserName. If the account belongs to the built-in domain, the name can be of the form .\UserName.
    user_account = TextField()

    class Meta:
        table_name = "services"
