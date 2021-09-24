"""
OSQuery sharing_preferences ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField


class SharingPreferences(BaseModel):
    """
    OS X Sharing preferences.
    """
    # 1 If screen sharing is enabled else 0
    screen_sharing = IntegerField()
    # 1 If file sharing is enabled else 0
    file_sharing = IntegerField()
    # 1 If printer sharing is enabled else 0
    printer_sharing = IntegerField()
    # 1 If remote login is enabled else 0
    remote_login = IntegerField()
    # 1 If remote management is enabled else 0
    remote_management = IntegerField()
    # 1 If remote apple events are enabled else 0
    remote_apple_events = IntegerField()
    # 1 If internet sharing is enabled else 0
    internet_sharing = IntegerField()
    # 1 If bluetooth sharing is enabled for any user else 0
    bluetooth_sharing = IntegerField()
    # 1 If CD or DVD sharing is enabled else 0
    disc_sharing = IntegerField()
    # 1 If content caching is enabled else 0
    content_caching = IntegerField()

    class Meta:
        table_name = "sharing_preferences"
