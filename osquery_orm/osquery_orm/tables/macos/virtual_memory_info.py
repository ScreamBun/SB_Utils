"""
OSQuery virtual_memory_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import BigIntegerField


class VirtualMemoryInfo(BaseModel):
    """
    Darwin Virtual Memory statistics.
    Examples:
        select * from virtual_memory_info;
    """
    # Total number of free pages.
    free = BigIntegerField()
    # Total number of active pages.
    active = BigIntegerField()
    # Total number of inactive pages.
    inactive = BigIntegerField()
    # Total number of speculative pages.
    speculative = BigIntegerField()
    # Total number of throttled pages.
    throttled = BigIntegerField()
    # Total number of wired down pages.
    wired = BigIntegerField()
    # Total number of purgeable pages.
    purgeable = BigIntegerField()
    # Total number of calls to vm_faults.
    faults = BigIntegerField()
    # Total number of copy-on-write pages.
    copy = BigIntegerField()
    # Total number of zero filled pages.
    zero_fill = BigIntegerField()
    # Total number of reactivated pages.
    reactivated = BigIntegerField()
    # Total number of purged pages.
    purged = BigIntegerField()
    # Total number of file backed pages.
    file_backed = BigIntegerField()
    # Total number of anonymous pages.
    anonymous = BigIntegerField()
    # Total number of uncompressed pages.
    uncompressed = BigIntegerField()
    # The number of pages used to store compressed VM pages.
    compressor = BigIntegerField()
    # The total number of pages that have been decompressed by the VM compressor.
    decompressed = BigIntegerField()
    # The total number of pages that have been compressed by the VM compressor.
    compressed = BigIntegerField()
    # The total number of requests for pages from a pager.
    page_ins = BigIntegerField()
    # Total number of pages paged out.
    page_outs = BigIntegerField()
    # The total number of compressed pages that have been swapped out to disk.
    swap_ins = BigIntegerField()
    # The total number of compressed pages that have been swapped back in from disk.
    swap_outs = BigIntegerField()

    class Meta:
        table_name = "virtual_memory_info"
