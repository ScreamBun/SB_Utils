"""
OSQuery mdls ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Mdls(BaseModel):
    """
    Query file metadata in the Spotlight database.
    Examples:
        select * from mdls where path = '/Users/testuser/Desktop/testfile';
    """
    # Path of the file
    path = TextField()  # {'required': True}
    # Name of the metadata key
    key = TextField()
    # Value stored in the metadata key
    value = TextField()
    # CoreFoundation type of data stored in value
    valuetype = TextField()  # {'hidden': True}

    class Meta:
        table_name = "mdls"
