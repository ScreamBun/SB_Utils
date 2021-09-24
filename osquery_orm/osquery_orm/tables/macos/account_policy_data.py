"""
OSQuery account_policy_data ORM
"""
from osquery_orm.orm import BaseModel
from peewee import DoubleField, BigIntegerField, ForeignKeyField
from ..cross_platform import MacOS_Users


class AccountPolicyData(BaseModel):
    """
    Additional OS X user account data from the AccountPolicy section of OpenDirectory.
    Examples:
        select * from users join account_policy_data using (uid)
    """
    # User ID
    uid = BigIntegerField()
    # When the account was first created
    creation_time = DoubleField()
    # The number of failed login attempts using an incorrect password. Count resets after a correct password is entered.
    failed_login_count = BigIntegerField()
    # The time of the last failed login attempt. Resets after a correct password is entered
    failed_login_timestamp = DoubleField()
    # The time the password was last changed
    password_last_set_time = DoubleField()
    account_policy_data = ForeignKeyField(MacOS_Users, backref='uid')

    class Meta:
        table_name = "account_policy_data"
