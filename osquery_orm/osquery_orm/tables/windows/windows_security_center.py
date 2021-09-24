"""
OSQuery windows_security_center ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class WindowsSecurityCenter(BaseModel):
    """
    The health status of Window Security features. Health values can be "Good", "Poor". "Snoozed", "Not Monitored", and "Error".
    Examples:
        select * from windows_security_center
    """
    # The health of the monitored Firewall (see windows_security_products)
    firewall = TextField()
    # The health of the Windows Autoupdate feature
    autoupdate = TextField()
    # The health of the monitored Antivirus solution (see windows_security_products)
    antivirus = TextField()
    # The health of the monitored Antispyware solution (see windows_security_products)
    antispyware = TextField()
    # The health of the Internet Settings
    internet_settings = TextField()
    # The health of the Windows Security Center Service
    windows_security_center_service = TextField()
    # The health of the User Account Control (UAC) capability in Windows
    user_account_control = TextField()

    class Meta:
        table_name = "windows_security_center"
