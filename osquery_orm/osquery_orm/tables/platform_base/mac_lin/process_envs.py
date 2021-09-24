"""
OSQuery process_envs ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class ProcessEnvs(BaseModel):
    """
    A key/value table of environment variables for each process.
    Examples:
        select * from process_envs where pid = 1
        select pe.*
             from process_envs pe, (select * from processes limit 10) p
             where p.pid = pe.pid;
    """
    # Process (or thread) ID
    pid = IntegerField()  # {'index': True}
    # Environment variable name
    key = TextField()
    # Environment variable value
    value = TextField()

    class Meta:
        table_name = "process_envs"
