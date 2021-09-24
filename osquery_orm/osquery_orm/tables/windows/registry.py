"""
OSQuery registry ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class Registry(BaseModel):
    """
    All of the Windows registry hives.
    Examples:
        select path, key, name from registry where key = 'HKEY_USERS'; -- get user SIDS. Note: path is key+name
        select path from registry where key like 'HKEY_USERS\.Default\%'; -- a SQL wildcard match; will not recurse subkeys
        select path from registry where key like 'HKEY_USERS\.Default\Software\%%'; -- recursing query (compare with 1 %)
        select path from registry where key like 'HKEY_LOCAL_MACHINE\Software\Micr%ft\%' and type = 'subkey' LIMIT 10; -- midfix wildcard match
        select name, type, data from registry where path like 'HKEY_USERS\%\Control Panel\International\\User Profile\Languages'; -- get users' current UI language. Note: osquery cannot reference HKEY_CURRENT_USER
        select name, type, data from registry where path like 'HKEY_USERS\%\Software\Microsoft\Windows\CurrentVersion\Explorer\Wallpapers\%';  -- list all of the desktop wallpapers
        select name, type, data from registry where key like 'HKEY_USERS\%\Software\Microsoft\Windows\CurrentVersion\Explorer\Wallpapers'; -- same, but filtering by key instead of path
    """
    # Name of the key to search for
    key = TextField()  # {'additional': True}
    # Full path to the value
    path = TextField()  # {'index': True}
    # Name of the registry value entry
    name = TextField()
    # Type of the registry value, or 'subkey' if item is a subkey
    type = TextField()
    # Data content of registry value
    data = TextField()
    # timestamp of the most recent registry write
    mtime = BigIntegerField()

    class Meta:
        table_name = "registry"