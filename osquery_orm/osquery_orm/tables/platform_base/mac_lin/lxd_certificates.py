"""
OSQuery lxd_certificates ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class LxdCertificates(BaseModel):
    """
    LXD certificates information.
    Examples:
        select * from lxd_certificates
    """
    # Name of the certificate
    name = TextField()
    # Type of the certificate
    type = TextField()
    # SHA256 hash of the certificate
    fingerprint = TextField()
    # Certificate content
    certificate = TextField()

    class Meta:
        table_name = "lxd_certificates"
