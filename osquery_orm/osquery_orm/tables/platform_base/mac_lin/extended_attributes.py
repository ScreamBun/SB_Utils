"""
OSQuery extended_attributes ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class ExtendedAttributes(BaseModel):
    """
    Returns the extended attributes for files (similar to Windows ADS).
    """
    # Absolute file path
    path = TextField()  # {'required': True}
    # Directory of file(s)
    directory = TextField()  # {'required': True}
    # Name of the value generated from the extended attribute
    key = TextField()
    # The parsed information from the attribute
    value = TextField()
    # 1 if the value is base64 encoded else 0
    base64 = IntegerField()

    class Meta:
        table_name = "extended_attributes"
