"""
OSQuery yara ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Yara(BaseModel):
    """
    Track YARA matches for files or PIDs.
    Examples:
        select * from yara where path = '/etc/passwd'
        select * from yara where path LIKE '/etc/%'
        select * from yara where path = '/etc/passwd' and sigfile = '/etc/osquery/yara/test.yara'
        select * from yara where path = '/etc/passwd' and sigrule = 'rule always_true { condition: true }'
    """
    # The path scanned
    path = TextField()  # {'index': True, 'required': True}
    # List of YARA matches
    matches = TextField()
    # Number of YARA matches
    count = IntegerField()
    # Signature group used
    sig_group = TextField()  # {'additional': True}
    # Signature file used
    sigfile = TextField()  # {'additional': True}
    # Signature strings used
    sigrule = TextField()  # {'additional': True, 'hidden': True}
    # Matching strings
    strings = TextField()
    # Matching tags
    tags = TextField()
    # Signature url
    sigurl = TextField()  # {'additional': True, 'hidden': True}

    class Meta:
        table_name = "yara"
