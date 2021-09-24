"""
OSQuery pipes ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Pipes(BaseModel):
    """
    Named and Anonymous pipes.
    Examples:
        select * from pipes
    """
    # Process ID of the process to which the pipe belongs
    pid = BigIntegerField()  # {'index': True}
    # Name of the pipe
    name = TextField()
    # Number of instances of the named pipe
    instances = IntegerField()
    # The maximum number of instances creatable for this pipe
    max_instances = IntegerField()
    # The flags indicating whether this pipe connection is a server or client end, and if the pipe for sending messages or bytes
    flags = TextField()

    class Meta:
        table_name = "pipes"
