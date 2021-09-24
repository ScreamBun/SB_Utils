"""
OSQuery cpu_time ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField


class CpuTime(BaseModel):
    """
    Displays information from /proc/stat file about the time the cpu cores spent in different parts of the system.
    """
    # Name of the cpu (core)
    core = IntegerField()
    # Time spent in user mode
    user = BigIntegerField()
    # Time spent in user mode with low priority (nice)
    nice = BigIntegerField()
    # Time spent in system mode
    system = BigIntegerField()
    # Time spent in the idle task
    idle = BigIntegerField()
    # Time spent waiting for I/O to complete
    iowait = BigIntegerField()
    # Time spent servicing interrupts
    irq = BigIntegerField()
    # Time spent servicing softirqs
    softirq = BigIntegerField()
    # Time spent in other operating systems when running in a virtualized environment
    steal = BigIntegerField()
    # Time spent running a virtual CPU for a guest OS under the control of the Linux kernel
    guest = BigIntegerField()
    # Time spent running a niced guest 
    guest_nice = BigIntegerField()

    class Meta:
        table_name = "cpu_time"
