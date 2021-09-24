"""
OSQuery python_packages ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class PythonPackages(BaseModel):
    """
    Python packages installed in a system.
    Examples:
        select * from python_packages where directory='/usr/'
    """
    # Package display name
    name = TextField()
    # Package-supplied version
    version = TextField()
    # Package-supplied summary
    summary = TextField()
    # Optional package author
    author = TextField()
    # License under which package is launched
    license = TextField()
    # Path at which this module resides
    path = TextField()
    # Directory where Python modules are located
    directory = TextField()  # {'index': True}

    class Meta:
        table_name = "python_packages"
