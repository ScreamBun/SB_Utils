"""
OSQuery quicklook_cache ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class QuicklookCache(BaseModel):
    """
    Files and thumbnails within OS X's Quicklook Cache.
    """
    # Path of file
    path = TextField()
    # Quicklook file rowid key
    rowid = IntegerField()
    # Quicklook file fs_id key
    fs_id = TextField()
    # Parsed volume ID from fs_id
    volume_id = IntegerField()
    # Parsed file ID (inode) from fs_id
    inode = IntegerField()
    # Parsed version date field
    mtime = IntegerField()
    # Parsed version size field
    size = BigIntegerField()
    # Parsed version 'gen' field
    label = TextField()
    # Apple date format for last thumbnail cache hit
    last_hit_date = IntegerField()
    # Number of cache hits on thumbnail
    hit_count = TextField()
    # Thumbnail icon mode
    icon_mode = BigIntegerField()
    # Path to cache data
    cache_path = TextField()

    class Meta:
        table_name = "quicklook_cache"
