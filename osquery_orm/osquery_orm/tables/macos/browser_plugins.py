"""
OSQuery browser_plugins ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, ForeignKeyField, TextField
from ..cross_platform import MacOS_Users


class BrowserPlugins(BaseModel):
    """
    All C/NPAPI browser plugin details for all users.
    Examples:
        select * from users join browser_plugins using (uid)
    """
    # The local user that owns the plugin
    uid = BigIntegerField()  # {'index': True}
    # Plugin display name
    name = TextField()
    # Plugin identifier
    identifier = TextField()
    # Plugin short version
    version = TextField()
    # Build SDK used to compile plugin
    sdk = TextField()
    # Plugin description text
    description = TextField()
    # Plugin language-localization
    development_region = TextField()
    # Plugin requires native execution
    native = IntegerField()
    # Path to plugin bundle
    path = TextField()  # {'index': True}
    # Is the plugin disabled. 1 = Disabled
    disabled = IntegerField()
    browser_plugins = ForeignKeyField(MacOS_Users, backref='uid')

    class Meta:
        table_name = "browser_plugins"
