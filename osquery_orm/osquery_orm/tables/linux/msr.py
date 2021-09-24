"""
OSQuery msr ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField


class Msr(BaseModel):
    """
    Various pieces of data stored in the model specific register per processor. NOTE: the msr kernel module must be enabled, and osquery must be run as root.
    """
    # The processor number as reported in /proc/cpuinfo
    processor_number = BigIntegerField()
    # Whether the turbo feature is disabled.
    turbo_disabled = BigIntegerField()
    # The turbo feature ratio limit.
    turbo_ratio_limit = BigIntegerField()
    # Platform information.
    platform_info = BigIntegerField()
    # Performance setting for the processor.
    perf_ctl = BigIntegerField()
    # Performance status for the processor.
    perf_status = BigIntegerField()
    # Bitfield controlling enabled features.
    feature_control = BigIntegerField()
    # Run Time Average Power Limiting power limit.
    rapl_power_limit = BigIntegerField()
    # Run Time Average Power Limiting energy status.
    rapl_energy_status = BigIntegerField()
    # Run Time Average Power Limiting power units.
    rapl_power_units = BigIntegerField()

    class Meta:
        table_name = "msr"
