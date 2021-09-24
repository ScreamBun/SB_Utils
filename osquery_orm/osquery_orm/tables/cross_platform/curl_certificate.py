"""
OSQuery curl_certificate ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class CurlCertificate(BaseModel):
    """
    Inspect TLS certificates by connecting to input hostnames.
    Examples:
        select * from curl_certificate where hostname = 'osquery.io'select * from curl_certificate where hostname = 'osquery.io' and dump_certificate = 1
    """
    # Hostname (domain[:port]) to CURL
    hostname = TextField()  # {'required': True}
    # Common name of company issued to
    common_name = TextField()
    # Organization issued to
    organization = TextField()
    # Organization unit issued to
    organization_unit = TextField()
    # Certificate serial number
    serial_number = TextField()
    # Issuer common name
    issuer_common_name = TextField()
    # Issuer organization
    issuer_organization = TextField()
    # Issuer organization unit
    issuer_organization_unit = TextField()
    # Period of validity start date
    valid_from = TextField()
    # Period of validity end date
    valid_to = TextField()
    # SHA-256 fingerprint
    sha256_fingerprint = TextField()
    # SHA1 fingerprint
    sha1_fingerprint = TextField()
    # Version Number
    version = IntegerField()
    # Signature Algorithm
    signature_algorithm = TextField()
    # Signature
    signature = TextField()
    # Subject Key Identifier
    subject_key_identifier = TextField()
    # Authority Key Identifier
    authority_key_identifier = TextField()
    # Usage of key in certificate
    key_usage = TextField()
    # Extended usage of key in certificate
    extended_key_usage = TextField()
    # Certificate Policies
    policies = TextField()
    # Subject Alternative Name
    subject_alternative_names = TextField()
    # Issuer Alternative Name
    issuer_alternative_names = TextField()
    # Authority Information Access
    info_access = TextField()
    # Subject Information Access
    subject_info_access = TextField()
    # Policy Mappings
    policy_mappings = TextField()
    # 1 if the certificate has expired, 0 otherwise
    has_expired = IntegerField()
    # Basic Constraints
    basic_constraint = TextField()
    # Name Constraints
    name_constraints = TextField()
    # Policy Constraints
    policy_constraints = TextField()
    # Set this value to '1' to dump certificate
    dump_certificate = IntegerField()  # {'additional': True, 'hidden': True}
    # Set this value to the timeout in seconds to complete the TLS handshake (default 4s, use 0 for no timeout)
    timeout = IntegerField()  # {'additional': True, 'hidden': True}
    # Certificate PEM format
    pem = TextField()

    class Meta:
        table_name = "curl_certificate"
