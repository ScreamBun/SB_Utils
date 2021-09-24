"""
OSQuery cpu_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class CpuInfo(BaseModel):
    """
    Retrieve cpu hardware info of the machine.
    """
    # The DeviceID of the CPU.
    device_id = TextField()
    # The model of the CPU.
    model = TextField()
    # The manufacturer of the CPU.
    manufacturer = TextField()
    # The processor type, such as Central, Math, or Video.
    processor_type = TextField()
    # The availability and status of the CPU.
    availability = TextField()
    # The current operating status of the CPU.
    cpu_status = IntegerField()
    # The number of cores of the CPU.
    number_of_cores = TextField()
    # The number of logical processors of the CPU.
    logical_processors = IntegerField()
    # The width of the CPU address bus.
    address_width = TextField()
    # The current frequency of the CPU.
    current_clock_speed = IntegerField()
    # The maximum possible frequency of the CPU.
    max_clock_speed = IntegerField()
    # The assigned socket on the board for the given CPU.
    socket_designation = TextField()

    class Meta:
        table_name = "cpu_info"
