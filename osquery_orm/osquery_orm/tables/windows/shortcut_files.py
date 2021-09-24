"""
OSQuery shortcut_files ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class ShortcutFiles(BaseModel):
    """
    View data about Windows Shortcut files.
    Examples:
        select * from shortcut_files;
    """
    # Directory name.
    path = TextField()  # {'required': True}
    # Target file path
    target_path = TextField()
    # Target Modified time.
    target_modified = IntegerField()
    # Target Created time.
    target_created = IntegerField()
    # Target Accessed time.
    target_accessed = IntegerField()
    # Size of target file.
    target_size = BigIntegerField()
    # Relative path to target file from lnk file.
    relative_path = TextField()
    # Local system path to target file.
    local_path = TextField()
    # Target file directory.
    working_path = TextField()
    # Lnk file icon location.
    icon_path = TextField()
    # Common system path to target file.
    common_path = TextField()
    # Command args passed to lnk file.
    command_args = TextField()
    # Optional hostname of the target file.
    hostname = TextField()
    # Share name of the target file.
    share_name = TextField()
    # Device containing the target file.
    device_type = TextField()
    # Volume serial number.
    volume_serial = TextField()
    # Target mft entry.
    mft_entry = BigIntegerField()
    # Target mft sequence.
    mft_sequence = IntegerField()
    # Lnk file description.
    description = TextField()

    class Meta:
        table_name = "shortcut_files"
