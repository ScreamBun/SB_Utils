"""
OSQuery signature ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Signature(BaseModel):
    """
    File (executable, bundle, installer, disk) code signing status.
    Examples:
        SELECT * FROM signature WHERE path = '/bin/ls'
        SELECT * FROM signature WHERE path = '/Applications/Xcode.app' AND hash_resources=0
        SELECT * FROM (SELECT path, MIN(signed) AS all_signed, MIN(CASE WHEN authority = 'Software Signing' AND signed = 1 THEN 1 ELSE 0 END) AS all_signed_by_apple FROM signature WHERE path LIKE '/bin/%' GROUP BY path);
    """
    # Must provide a path or directory
    path = TextField()  # {'index': True, 'required': True}
    # Set to 1 to also hash resources, or 0 otherwise. Default is 1
    hash_resources = IntegerField()  # {'additional': True}
    # If applicable, the arch of the signed code
    arch = TextField()
    # 1 If the file is signed else 0
    signed = IntegerField()
    # The signing identifier sealed into the signature
    identifier = TextField()
    # Hash of the application Code Directory
    cdhash = TextField()
    # The team signing identifier sealed into the signature
    team_identifier = TextField()
    # Certificate Common Name
    authority = TextField()

    class Meta:
        table_name = "signature"
