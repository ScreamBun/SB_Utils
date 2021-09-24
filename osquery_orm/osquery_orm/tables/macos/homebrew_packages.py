"""
OSQuery homebrew_packages ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class HomebrewPackages(BaseModel):
    """
    The installed homebrew package database.
    """
    # Package name
    name = TextField()
    # Package install path
    path = TextField()
    # Current 'linked' version
    version = TextField()
    # Homebrew install prefix
    prefix = TextField()  # {'hidden': True, 'additional': True}

    class Meta:
        table_name = "homebrew_packages"
