"""
OSQuery wifi_networks ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class WifiNetworks(BaseModel):
    """
    OS X known/remembered Wi-Fi networks list.
    """
    # SSID octets of the network
    ssid = TextField()
    # Name of the network
    network_name = TextField()
    # Type of security on this network
    security_type = TextField()
    # Last time this netword was connected to as a unix_time
    last_connected = IntegerField()
    # 1 if Passpoint is supported, 0 otherwise
    passpoint = IntegerField()
    # 1 if network is possibly a hidden network, 0 otherwise
    possibly_hidden = IntegerField()
    # 1 if roaming is supported, 0 otherwise
    roaming = IntegerField()
    # Describe the roaming profile, usually one of Single, Dual  or Multi
    roaming_profile = TextField()
    # 1 if this network has a captive portal, 0 otherwise
    captive_portal = IntegerField()
    # 1 if auto login is enabled, 0 otherwise
    auto_login = IntegerField()
    # 1 if this network is temporarily disabled, 0 otherwise
    temporarily_disabled = IntegerField()
    # 1 if this network is disabled, 0 otherwise
    disabled = IntegerField()

    class Meta:
        table_name = "wifi_networks"
