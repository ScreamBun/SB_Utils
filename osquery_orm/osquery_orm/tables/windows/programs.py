"""
OSQuery programs ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Programs(BaseModel):
    """
    Represents products as they are installed by Windows Installer. A product generally correlates to one installation package on Windows. Some fields may be blank as Windows installation details are left to the discretion of the product author.
    Examples:
        select * from programs
        select name, install_location from programs where install_location not like 'C:\Program Files%';
    """
    # Commonly used product name.
    name = TextField()
    # Product version information.
    version = TextField()
    # The installation location directory of the product.
    install_location = TextField()
    # The installation source of the product.
    install_source = TextField()
    # The language of the product.
    language = TextField()
    # Name of the product supplier.
    publisher = TextField()
    # Path and filename of the uninstaller.
    uninstall_string = TextField()
    # Date that this product was installed on the system. 
    install_date = TextField()
    # Product identification such as a serial number on software, or a die number on a hardware chip.
    identifying_number = TextField()

    class Meta:
        table_name = "programs"
