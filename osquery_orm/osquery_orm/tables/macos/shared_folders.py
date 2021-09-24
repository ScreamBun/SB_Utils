"""
OSQuery shared_folders ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class SharedFolders(BaseModel):
    """
    Folders available to others via SMB or AFP.
    """
    # The shared name of the folder as it appears to other users
    name = TextField()
    # Absolute path of shared folder on the local system
    path = TextField()

    class Meta:
        table_name = "shared_folders"
