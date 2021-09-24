"""
OSQuery systemd_units ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField, TextField


class SystemdUnits(BaseModel):
    """
    Track systemd units.
    """
    # Unique unit identifier
    id = TextField()
    # Unit description
    description = TextField()
    # Reflects whether the unit definition was properly loaded
    load_state = TextField()
    # The high-level unit activation state, i.e. generalization of SUB
    active_state = TextField()
    # The low-level unit activation state, values depend on unit type
    sub_state = TextField()
    # The name of another unit that this unit follows in state
    following = TextField()
    # The object path for this unit
    object_path = TextField()
    # Next queued job id
    job_id = BigIntegerField()
    # Job type
    job_type = TextField()
    # The object path for the job
    job_path = TextField()
    # The unit file path this unit was read from, if there is any
    fragment_path = TextField()
    # The configured user, if any
    user = TextField()
    # Path to the (possibly generated) unit configuration file
    source_path = TextField()

    class Meta:
        table_name = "systemd_units"
