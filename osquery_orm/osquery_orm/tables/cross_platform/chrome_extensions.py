"""
OSQuery chrome_extensions ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, ForeignKeyField, TextField
from .users import Users


class ChromeExtensions(BaseModel):
    """
    Chrome-based browser extensions.
    Examples:
        select * from users join chrome_extensions using (uid)
    """
    # The browser type (Valid values: chrome, chromium, opera, yandex, brave, edge, edge_beta)
    browser_type = TextField()
    # The local user that owns the extension
    uid = BigIntegerField()  # {'index': True}
    # Extension display name
    name = TextField()
    # The name of the Chrome profile that contains this extension
    profile = TextField()
    # The profile path
    profile_path = TextField()
    # Extension identifier, as specified by the preferences file. Empty if the extension is not in the profile.
    referenced_identifier = TextField()
    # Extension identifier, computed from its manifest. Empty in case of error.
    identifier = TextField()
    # Extension-supplied version
    version = TextField()
    # Extension-optional description
    description = TextField()
    # Default locale supported by extension
    default_locale = TextField()  # {'aliases': ['locale']}
    # Current locale supported by extension
    current_locale = TextField()
    # Extension-supplied update URI
    update_url = TextField()
    # Optional extension author
    author = TextField()
    # 1 If extension is persistent across all tabs else 0
    persistent = IntegerField()
    # Path to extension folder
    path = TextField()
    # The permissions required by the extension
    permissions = TextField()
    # The JSON-encoded permissions required by the extension
    permissions_json = TextField()  # {'hidden': True}
    # The permissions optionally required by the extensions
    optional_permissions = TextField()
    # The JSON-encoded permissions optionally required by the extensions
    optional_permissions_json = TextField()  # {'hidden': True}
    # The SHA256 hash of the manifest.json file
    manifest_hash = TextField()
    # 1 if this extension is referenced by the Preferences file of the profile
    referenced = BigIntegerField()
    # True if this extension was installed from the web store
    from_webstore = TextField()
    # 1 if this extension is enabled
    state = TextField()
    # Extension install time, in its original Webkit format
    install_time = TextField()
    # Extension install time, converted to unix time
    install_timestamp = BigIntegerField()
    # The manifest file of the extension
    manifest_json = TextField()  # {'hidden': True}
    # The extension key, from the manifest file
    key = TextField()  # {'hidden': True}
    chrome_extensions = ForeignKeyField(Users, backref='uid')

    class Meta:
        table_name = "chrome_extensions"
