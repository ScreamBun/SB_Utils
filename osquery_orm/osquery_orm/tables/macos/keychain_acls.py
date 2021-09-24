"""
OSQuery keychain_acls ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class KeychainAcls(BaseModel):
    """
    Applications that have ACL entries in the keychain.
    Examples:
        select label, description, authorizations, path, count(path) as c from keychain_acls where label != '' and path != '' group by label having c > 1;
    """
    # The path of the keychain
    keychain_path = TextField()
    # A space delimited set of authorization attributes
    authorizations = TextField()
    # The path of the authorized application
    path = TextField()
    # The description included with the ACL entry
    description = TextField()
    # An optional label tag that may be included with the keychain entry
    label = TextField()

    class Meta:
        table_name = "keychain_acls"
