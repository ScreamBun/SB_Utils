"""
OSQuery apparmor_profiles ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class ApparmorProfiles(BaseModel):
    """
    Track active AppArmor profiles.
    Examples:
        SELECT * FROM apparmor_profiles WHERE mode = 'complain'
    """
    # Unique, aa-status compatible, policy identifier.
    path = TextField()  # {'index': True}
    # Policy name.
    name = TextField()
    # Which executable(s) a profile will attach to.
    attach = TextField()
    # How the policy is applied.
    mode = TextField()
    # A unique hash that identifies this policy.
    sha1 = TextField()

    class Meta:
        table_name = "apparmor_profiles"
