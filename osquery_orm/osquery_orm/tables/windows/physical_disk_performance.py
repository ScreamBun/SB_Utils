"""
OSQuery physical_disk_performance ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class PhysicalDiskPerformance(BaseModel):
    """
    Provides provides raw data from performance counters that monitor hard or fixed disk drives on the system.
    """
    # Name of the physical disk
    name = TextField()
    # Average number of bytes transferred from the disk during read operations
    avg_disk_bytes_per_read = BigIntegerField()
    # Average number of bytes transferred to the disk during write operations
    avg_disk_bytes_per_write = BigIntegerField()
    # Average number of read requests that were queued for the selected disk during the sample interval
    avg_disk_read_queue_length = BigIntegerField()
    # Average number of write requests that were queued for the selected disk during the sample interval
    avg_disk_write_queue_length = BigIntegerField()
    # Average time, in seconds, of a read operation of data from the disk
    avg_disk_sec_per_read = IntegerField()
    # Average time, in seconds, of a write operation of data to the disk
    avg_disk_sec_per_write = IntegerField()
    # Number of requests outstanding on the disk at the time the performance data is collected
    current_disk_queue_length = IntegerField()
    # Percentage of elapsed time that the selected disk drive is busy servicing read requests
    percent_disk_read_time = BigIntegerField()
    # Percentage of elapsed time that the selected disk drive is busy servicing write requests
    percent_disk_write_time = BigIntegerField()
    # Percentage of elapsed time that the selected disk drive is busy servicing read or write requests
    percent_disk_time = BigIntegerField()
    # Percentage of time during the sample interval that the disk was idle
    percent_idle_time = BigIntegerField()

    class Meta:
        table_name = "physical_disk_performance"
