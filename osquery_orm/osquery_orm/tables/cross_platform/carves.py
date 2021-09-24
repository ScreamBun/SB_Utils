"""
OSQuery carves ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Carves(BaseModel):
    """
    List the set of completed and in-progress carves. If carve=1 then the query is treated as a new carve request.
    Examples:
        select * from carves
        select * from carves where status like '%FAIL%'
        select * from carves where path like '/Users/%/Downloads/%' and carve=1
    """
    # Time at which the carve was kicked off
    time = BigIntegerField()
    # A SHA256 sum of the carved archive
    sha256 = TextField()
    # Size of the carved archive
    size = IntegerField()
    # The path of the requested carve
    path = TextField()  # {'additional': True}
    # Status of the carve, can be STARTING, PENDING, SUCCESS, or FAILED
    status = TextField()
    # Identifying value of the carve session
    carve_guid = TextField()  # {'index': True}
    # Identifying value of the carve request (e.g., scheduled query name, distributed request, etc)
    request_id = TextField()
    # Set this value to '1' to start a file carve
    carve = IntegerField()  # {'additional': True}

    class Meta:
        table_name = "carves"
