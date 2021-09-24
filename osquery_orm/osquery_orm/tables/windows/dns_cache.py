"""
OSQuery dns_cache ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class DnsCache(BaseModel):
    """
    Enumerate the DNS cache using the undocumented DnsGetCacheDataTable function in dnsapi.dll.
    Examples:
        select * from dns_cache
    """
    # DNS record name
    name = TextField()
    # DNS record type
    type = TextField()
    # DNS record flags
    flags = IntegerField()

    class Meta:
        table_name = "dns_cache"
