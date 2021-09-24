"""
OSQuery ntdomains ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Ntdomains(BaseModel):
    """
    Display basic NT domain information of a Windows machine.
    Examples:
        select * from ntdomains
    """
    # The label by which the object is known.
    name = TextField()
    # The name of the site where the domain controller is configured.
    client_site_name = TextField()
    # The name of the site where the domain controller is located.
    dc_site_name = TextField()
    # The name of the root of the DNS tree.
    dns_forest_name = TextField()
    # The IP Address of the discovered domain controller..
    domain_controller_address = TextField()
    # The name of the discovered domain controller.
    domain_controller_name = TextField()
    # The name of the domain.
    domain_name = TextField()
    # The current status of the domain object.
    status = TextField()

    class Meta:
        table_name = "ntdomains"
