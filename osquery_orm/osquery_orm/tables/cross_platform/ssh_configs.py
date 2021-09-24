"""
OSQuery ssh_configs ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, ForeignKeyField, TextField
from .users import Users


class SshConfigs(BaseModel):
    """
    A table of parsed ssh_configs.
    Examples:
        select * from users join ssh_configs using (uid)
    """
    # The local owner of the ssh_config file
    uid = BigIntegerField()  # {'additional': True}
    # The host or match block
    block = TextField()
    # The option and value
    option = TextField()
    # Path to the ssh_config file
    ssh_config_file = TextField()
    ssh_configs = ForeignKeyField(Users, backref='uid')

    class Meta:
        table_name = "ssh_configs"
