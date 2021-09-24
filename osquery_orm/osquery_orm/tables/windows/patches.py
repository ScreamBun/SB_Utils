"""
OSQuery patches ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Patches(BaseModel):
    """
    Lists all the patches applied. Note: This does not include patches applied via MSI or downloaded from Windows Update (e.g. Service Packs).
    Examples:
        select * from patches
    """
    # The name of the host the patch is installed on.
    csname = TextField()
    # The KB ID of the patch.
    hotfix_id = TextField()
    # Short description of the patch.
    caption = TextField()
    # Fuller description of the patch.
    description = TextField()
    # Additional comments about the patch.
    fix_comments = TextField()
    # The system context in which the patch as installed.
    installed_by = TextField()
    # Indicates when the patch was installed. Lack of a value does not indicate that the patch was not installed.
    install_date = TextField()
    # The date when the patch was installed.
    installed_on = TextField()

    class Meta:
        table_name = "patches"
