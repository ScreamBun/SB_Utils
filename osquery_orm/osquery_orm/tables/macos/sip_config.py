"""
OSQuery sip_config ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class SipConfig(BaseModel):
    """
    Apple's System Integrity Protection (rootless) status.
    Examples:
        select * from sip_config
    """
    # The System Integrity Protection config flag
    config_flag = TextField()
    # 1 if this configuration is enabled, otherwise 0
    enabled = IntegerField()
    # 1 if this configuration is enabled, otherwise 0
    enabled_nvram = IntegerField()

    class Meta:
        table_name = "sip_config"
