"""
OSQuery iptables ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class Iptables(BaseModel):
    """
    Linux IP packet filtering and NAT tool.
    """
    # Packet matching filter table name.
    filter_name = TextField()
    # Size of module content.
    chain = TextField()
    # Policy that applies for this rule.
    policy = TextField()
    # Target that applies for this rule.
    target = TextField()
    # Protocol number identification.
    protocol = IntegerField()
    # Protocol source port(s).
    src_port = TextField()
    # Protocol destination port(s).
    dst_port = TextField()
    # Source IP address.
    src_ip = TextField()
    # Source IP address mask.
    src_mask = TextField()
    # Input interface for the rule.
    iniface = TextField()
    # Input interface mask for the rule.
    iniface_mask = TextField()
    # Destination IP address.
    dst_ip = TextField()
    # Destination IP address mask.
    dst_mask = TextField()
    # Output interface for the rule.
    outiface = TextField()
    # Output interface mask for the rule.
    outiface_mask = TextField()
    # Matching rule that applies.
    match = TextField()
    # Number of matching packets for this rule.
    packets = IntegerField()
    # Number of matching bytes for this rule.
    bytes = IntegerField()

    class Meta:
        table_name = "iptables"
