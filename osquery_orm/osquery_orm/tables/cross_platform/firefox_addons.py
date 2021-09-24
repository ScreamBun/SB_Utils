"""
OSQuery firefox_addons ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, ForeignKeyField, TextField
from .users import Users


class FirefoxAddons(BaseModel):
    """
    Firefox browser extensions, webapps, and addons.
    Examples:
        select * from users join firefox_addons using (uid)
    """
    # The local user that owns the addon
    uid = BigIntegerField()  # {'additional': True}
    # Addon display name
    name = TextField()
    # Addon identifier
    identifier = TextField()  # {'index': True}
    # Addon-supported creator string
    creator = TextField()
    # Extension, addon, webapp
    type = TextField()
    # Addon-supplied version string
    version = TextField()
    # Addon-supplied description string
    description = TextField()
    # URL that installed the addon
    source_url = TextField()
    # 1 If the addon is shown in browser else 0
    visible = IntegerField()
    # 1 If the addon is active else 0
    active = IntegerField()
    # 1 If the addon is application-disabled else 0
    disabled = IntegerField()
    # 1 If the addon applies background updates else 0
    autoupdate = IntegerField()
    # 1 If the addon includes binary components else 0
    native = IntegerField()
    # Global, profile location
    location = TextField()
    # Path to plugin bundle
    path = TextField()
    firefox_addons = ForeignKeyField(Users, backref='uid')

    class Meta:
        table_name = "firefox_addons"
