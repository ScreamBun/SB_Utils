"""
OSQuery gatekeeper ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Gatekeeper(BaseModel):
    """
    OS X Gatekeeper Details.
    """
    # 1 If a Gatekeeper is enabled else 0
    assessments_enabled = IntegerField()
    # 1 If a Gatekeeper allows execution from identified developers else 0
    dev_id_enabled = IntegerField()
    # Version of Gatekeeper's gke.bundle
    version = TextField()
    # Version of Gatekeeper's gkopaque.bundle
    opaque_version = TextField()

    class Meta:
        table_name = "gatekeeper"
