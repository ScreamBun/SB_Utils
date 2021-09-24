"""
OSQuery portage_keywords ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class PortageKeywords(BaseModel):
    """
    A summary about portage configurations like keywords, mask and unmask.
    """
    # Package name
    package = TextField()
    # The version which are affected by the use flags, empty means all
    version = TextField()
    # The keyword applied to the package
    keyword = TextField()
    # If the package is masked
    mask = IntegerField()
    # If the package is unmasked
    unmask = IntegerField()

    class Meta:
        table_name = "portage_keywords"
