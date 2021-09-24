"""
OSQuery certificates ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, DateTimeField, TextField


class Certificates(BaseModel):
    """
    Certificate Authorities installed in Keychains/ca-bundles.
    """
    # Certificate CommonName
    common_name = TextField()
    # Certificate distinguished name
    subject = TextField()
    # Certificate issuer distinguished name
    issuer = TextField()
    # 1 if CA: true (certificate is an authority) else 0
    ca = IntegerField()
    # 1 if self-signed, else 0
    self_signed = IntegerField()
    # Lower bound of valid date
    not_valid_before = DateTimeField()
    # Certificate expiration data
    not_valid_after = DateTimeField()
    # Signing algorithm used
    signing_algorithm = TextField()
    # Key algorithm used
    key_algorithm = TextField()
    # Key size used for RSA/DSA, or curve name
    key_strength = TextField()
    # Certificate key usage and extended key usage
    key_usage = TextField()
    # SKID an optionally included SHA1
    subject_key_id = TextField()
    # AKID an optionally included SHA1
    authority_key_id = TextField()
    # SHA1 hash of the raw certificate contents
    sha1 = TextField()
    # Path to Keychain or PEM bundle
    path = TextField()  # {'additional': True}
    # Certificate serial number
    serial = TextField()

    class Meta:
        table_name = "certificates"


# OS specific properties for Windows
class Windows_Certificates(Certificates):
    # SID
    sid = TextField()
    # Certificate system store location
    store_location = TextField()
    # Certificate system store
    store = TextField()
    # Username
    username = TextField()
    # Exists for service/user stores. Contains raw store id provided by WinAPI.
    store_id = TextField()
