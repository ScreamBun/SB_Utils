"""
OSQuery screenlock ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField


class Screenlock(BaseModel):
    """
    macOS screenlock status for the current logged in user context.
    """
    # 1 If a password is required after sleep or the screensaver begins; else 0
    enabled = IntegerField()
    # The amount of time in seconds the screen must be asleep or the screensaver on before a password is required on-wake. 0 = immediately; -1 = no password is required on-wake
    grace_period = IntegerField()

    class Meta:
        table_name = "screenlock"
