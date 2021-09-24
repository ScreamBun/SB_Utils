"""
OSQuery magic ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Magic(BaseModel):
    """
    Magic number recognition library table.
    """
    # Absolute path to target file
    path = TextField()  # {'required': True, 'index': True}
    # Colon(:) separated list of files where the magic db file can be found. By default one of the following is used: /usr/share/file/magic/magic, /usr/share/misc/magic or /usr/share/misc/magic.mgc
    magic_db_files = TextField()  # {'additional': True}
    # Magic number data from libmagic
    data = TextField()
    # MIME type data from libmagic
    mime_type = TextField()
    # MIME encoding data from libmagic
    mime_encoding = TextField()

    class Meta:
        table_name = "magic"
