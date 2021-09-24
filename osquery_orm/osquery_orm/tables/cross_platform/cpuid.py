"""
OSQuery cpuid ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Cpuid(BaseModel):
    """
    Useful CPU features from the cpuid ASM call.
    """
    # Present feature flags
    feature = TextField()
    # Bit value or string
    value = TextField()
    # Register used to for feature value
    output_register = TextField()
    # Bit in register value for feature value
    output_bit = IntegerField()
    # Value of EAX used
    input_eax = TextField()

    class Meta:
        table_name = "cpuid"
