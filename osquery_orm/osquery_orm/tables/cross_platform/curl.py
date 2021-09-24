"""
OSQuery curl ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class Curl(BaseModel):
    """
    Perform an http request and return stats about it.
    Examples:
        select url, round_trip_time, response_code from curl where url = 'https://github.com/osquery/osquery'
    """
    # The url for the request
    url = TextField()  # {'required': True, 'index': True}
    # The HTTP method for the request
    method = TextField()
    # The user-agent string to use for the request
    user_agent = TextField()  # {'additional': True}
    # The HTTP status code for the response
    response_code = IntegerField()
    # Time taken to complete the request
    round_trip_time = BigIntegerField()
    # Number of bytes in the response
    bytes = BigIntegerField()
    # The HTTP response body
    result = TextField()

    class Meta:
        table_name = "curl"
