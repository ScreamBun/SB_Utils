"""
OSQuery authenticode ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Authenticode(BaseModel):
    """
    File (executable, bundle, installer, disk) code signing status.
    Examples:
        SELECT * FROM authenticode WHERE path = 'C:\Windows\notepad.exe'
        SELECT process.pid, process.path, signature.result FROM processes as process LEFT JOIN authenticode AS signature ON process.path = signature.path;
    """
    # Must provide a path or directory
    path = TextField()  # {'required': True}
    # The original program name that the publisher has signed
    original_program_name = TextField()
    # The certificate serial number
    serial_number = TextField()
    # The certificate issuer name
    issuer_name = TextField()
    # The certificate subject name
    subject_name = TextField()
    # The signature check result
    result = TextField()

    class Meta:
        table_name = "authenticode"
