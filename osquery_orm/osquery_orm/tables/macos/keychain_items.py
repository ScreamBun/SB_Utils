"""
OSQuery keychain_items ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class KeychainItems(BaseModel):
    """
    Generic details about keychain items.
    """
    # Generic item name
    label = TextField()
    # Optional item description
    description = TextField()
    # Optional keychain comment
    comment = TextField()
    # Data item was created
    created = TextField()
    # Date of last modification
    modified = TextField()
    # Keychain item type (class)
    type = TextField()
    # Path to keychain containing item
    path = TextField()  # {'additional': True}

    class Meta:
        table_name = "keychain_items"
