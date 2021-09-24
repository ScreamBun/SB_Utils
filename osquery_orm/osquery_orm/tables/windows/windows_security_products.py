"""
OSQuery windows_security_products ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class WindowsSecurityProducts(BaseModel):
    """
    Enumeration of registered Windows security products.
    Examples:
        select * from windows_security_products
    """
    # Type of security product
    type = TextField()
    # Name of product
    name = TextField()
    # State of protection
    state = TextField()
    # Timestamp for the product state
    state_timestamp = TextField()
    # Remediation path
    remediation_path = TextField()
    # 1 if product signatures are up to date, else 0
    signatures_up_to_date = IntegerField()

    class Meta:
        table_name = "windows_security_products"
