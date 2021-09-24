"""
OSQuery arp_cache ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class ArpCache(BaseModel):
    """
    Address resolution cache, both static and dynamic (from ARP, NDP).
    """
    # IPv4 address target
    address = TextField()
    # MAC address of broadcasted address
    mac = TextField()
    # Interface of the network for the MAC
    interface = TextField()
    # 1 for true, 0 for false
    permanent = TextField()

    class Meta:
        table_name = "arp_cache"
