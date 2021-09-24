"""
OSQuery prefetch ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Prefetch(BaseModel):
    """
    Prefetch files show metadata related to file execution.
    Examples:
        select * from prefetch;
    """
    # Prefetch file path.
    path = TextField()  # {'additional': True}
    # Executable filename.
    filename = TextField()
    # Prefetch CRC hash.
    hash = TextField()
    # Most recent time application was run.
    last_run_time = IntegerField()
    # Other execution times in prefetch file.
    other_run_times = TextField()
    # Number of times the application has been run.
    run_count = IntegerField()
    # Application file size.
    size = IntegerField()
    # Volume serial number.
    volume_serial = TextField()
    # Volume creation time.
    volume_creation = TextField()
    # Number of files accessed.
    accessed_files_count = IntegerField()
    # Number of directories accessed.
    accessed_directories_count = IntegerField()
    # Files accessed by application within ten seconds of launch.
    accessed_files = TextField()
    # Directories accessed by application within ten seconds of launch.
    accessed_directories = TextField()

    class Meta:
        table_name = "prefetch"
