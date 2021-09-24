"""
OSQuery ad_config ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class AdConfig(BaseModel):
    """
    OS X Active Directory configuration.
    """
    # The OS X-specific configuration name
    name = TextField()
    # Active Directory trust domain
    domain = TextField()
    # Canonical name of option
    option = TextField()
    # Variable typed option value
    value = TextField()

    class Meta:
        table_name = "ad_config"
