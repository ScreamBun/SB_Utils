"""
OSQuery portage_use ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class PortageUse(BaseModel):
    """
    List of enabled portage USE values for specific package.
    """
    # Package name
    package = TextField()
    # The version of the installed package
    version = TextField()
    # USE flag which has been enabled for package
    use = TextField()

    class Meta:
        table_name = "portage_use"
