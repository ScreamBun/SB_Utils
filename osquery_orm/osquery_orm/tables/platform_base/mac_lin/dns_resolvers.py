"""
OSQuery dns_resolvers ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class DnsResolvers(BaseModel):
    """
    Resolvers used by this host.
    """
    # Address type index or order
    id = IntegerField()
    # Address type: sortlist, nameserver, search
    type = TextField()
    # Resolver IP/IPv6 address
    address = TextField()
    # Address (sortlist) netmask length
    netmask = TextField()
    # Resolver options
    options = BigIntegerField()

    class Meta:
        table_name = "dns_resolvers"
