"""
OSQuery interface_details ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class InterfaceDetails(BaseModel):
    """
    Detailed information and stats of network interfaces.
    Examples:
        select interface, mac, type, idrops as input_drops from interface_details;
        select interface, mac, type, flags, (1<<8) as promisc_flag from interface_details where (flags & promisc_flag) > 0;
        select interface, mac, type, flags, (1<<3) as loopback_flag from interface_details where (flags & loopback_flag) > 0;
    """
    # Interface name
    interface = TextField()
    # MAC of interface (optional)
    mac = TextField()
    # Interface type (includes virtual)
    type = IntegerField()
    # Network MTU
    mtu = IntegerField()
    # Metric based on the speed of the interface
    metric = IntegerField()
    # Flags (netdevice) for the device
    flags = IntegerField()
    # Input packets
    ipackets = BigIntegerField()
    # Output packets
    opackets = BigIntegerField()
    # Input bytes
    ibytes = BigIntegerField()
    # Output bytes
    obytes = BigIntegerField()
    # Input errors
    ierrors = BigIntegerField()
    # Output errors
    oerrors = BigIntegerField()
    # Input drops
    idrops = BigIntegerField()
    # Output drops
    odrops = BigIntegerField()
    # Packet Collisions detected
    collisions = BigIntegerField()
    # Time of last device modification (optional)
    last_change = BigIntegerField()

    class Meta:
        table_name = "interface_details"


# OS specific properties for Posix
class Posix_InterfaceDetails(InterfaceDetails):
    # Interface speed in Mb/s
    link_speed = BigIntegerField()


# OS specific properties for Linux
class Linux_InterfaceDetails(InterfaceDetails):
    # PCI slot number
    pci_slot = TextField()


# OS specific properties for Windows
class Windows_InterfaceDetails(InterfaceDetails):
    # The friendly display name of the interface.
    friendly_name = TextField()
    # Short description of the object a one-line string.
    description = TextField()
    # Name of the network adapter's manufacturer.
    manufacturer = TextField()
    # Name of the network connection as it appears in the Network Connections Control Panel program.
    connection_id = TextField()
    # State of the network adapter connection to the network.
    connection_status = TextField()
    # Indicates whether the adapter is enabled or not.
    enabled = IntegerField()
    # Indicates whether the adapter is a physical or a logical adapter.
    physical_adapter = IntegerField()
    # Estimate of the current bandwidth in bits per second.
    speed = IntegerField()
    # The name of the service the network adapter uses.
    service = TextField()
    # If TRUE, the dynamic host configuration protocol (DHCP) server automatically assigns an IP address to the computer system when establishing a network connection.
    dhcp_enabled = IntegerField()
    # Expiration date and time for a leased IP address that was assigned to the computer by the dynamic host configuration protocol (DHCP) server.
    dhcp_lease_expires = TextField()
    # Date and time the lease was obtained for the IP address assigned to the computer by the dynamic host configuration protocol (DHCP) server.
    dhcp_lease_obtained = TextField()
    # IP address of the dynamic host configuration protocol (DHCP) server.
    dhcp_server = TextField()
    # Organization name followed by a period and an extension that indicates the type of organization, such as 'microsoft.com'.
    dns_domain = TextField()
    # Array of DNS domain suffixes to be appended to the end of host names during name resolution.
    dns_domain_suffix_search_order = TextField()
    # Host name used to identify the local computer for authentication by some utilities.
    dns_host_name = TextField()
    # Array of server IP addresses to be used in querying for DNS servers.
    dns_server_search_order = TextField()
