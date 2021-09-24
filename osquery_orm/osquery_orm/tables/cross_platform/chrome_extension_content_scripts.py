"""
OSQuery chrome_extension_content_scripts ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, ForeignKeyField, TextField
from .users import Users


class ChromeExtensionContentScripts(BaseModel):
    """
    Chrome browser extension content scripts.
    Examples:
        SELECT chrome_extension_content_scripts.* FROM users JOIN chrome_extension_content_scripts USING (uid) GROUP BY identifier, match
    """
    # The browser type (Valid values: chrome, chromium, opera, yandex, brave)
    browser_type = TextField()
    # The local user that owns the extension
    uid = BigIntegerField()  # {'index': True}
    # Extension identifier
    identifier = TextField()
    # Extension-supplied version
    version = TextField()
    # The content script used by the extension
    script = TextField()
    # The pattern that the script is matched against
    match = TextField()
    # The profile path
    profile_path = TextField()
    # Path to extension folder
    path = TextField()
    # 1 if this extension is referenced by the Preferences file of the profile
    referenced = BigIntegerField()
    chrome_extension_content_scripts = ForeignKeyField(Users, backref='uid')

    class Meta:
        table_name = "chrome_extension_content_scripts"
