"""
OSQuery mdfind ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Mdfind(BaseModel):
    """
    Run searches against the spotlight database.
    Examples:
        select count(*) from mdfind where query = 'kMDItemTextContent == "osquery"';select * from mdfind where query = 'kMDItemDisplayName == "rook.stl"';
        select * from mdfind where query in ('kMDItemDisplayName == "rook.stl"', 'kMDItemDisplayName == "video.mp4"')
    """
    # Path of the file returned from spotlight
    path = TextField()
    # The query that was run to find the file
    query = TextField()  # {'required': True}

    class Meta:
        table_name = "mdfind"
