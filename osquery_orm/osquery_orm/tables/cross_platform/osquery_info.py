"""
OSQuery osquery_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class OsqueryInfo(BaseModel):
    """
    Top level information about the running version of osquery.
    """
    # Process (or thread/handle) ID
    pid = IntegerField()
    # Unique ID provided by the system
    uuid = TextField()
    # Unique, long-lived ID per instance of osquery
    instance_id = TextField()
    # osquery toolkit version
    version = TextField()
    # Hash of the working configuration state
    config_hash = TextField()
    # 1 if the config was loaded and considered valid, else 0
    config_valid = IntegerField()
    # osquery extensions status
    extensions = TextField()
    # osquery toolkit build platform
    build_platform = TextField()
    # osquery toolkit platform distribution name (os version)
    build_distro = TextField()
    # UNIX time in seconds when the process started
    start_time = IntegerField()
    # Process (or thread/handle) ID of optional watcher process
    watcher = IntegerField()
    # The osquery platform bitmask
    platform_mask = IntegerField()

    class Meta:
        table_name = "osquery_info"
