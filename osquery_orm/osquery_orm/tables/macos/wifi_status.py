"""
OSQuery wifi_status ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class WifiStatus(BaseModel):
    """
    OS X current WiFi status.
    """
    # Name of the interface
    interface = TextField()
    # SSID octets of the network
    ssid = TextField()
    # The current basic service set identifier
    bssid = TextField()
    # Name of the network
    network_name = TextField()
    # The country code (ISO/IEC 3166-1:1997) for the network
    country_code = TextField()
    # Type of security on this network
    security_type = TextField()
    # The current received signal strength indication (dbm)
    rssi = IntegerField()
    # The current noise measurement (dBm)
    noise = IntegerField()
    # Channel number
    channel = IntegerField()
    # Channel width
    channel_width = IntegerField()
    # Channel band
    channel_band = IntegerField()
    # The current transmit rate
    transmit_rate = TextField()
    # The current operating mode for the Wi-Fi interface
    mode = TextField()

    class Meta:
        table_name = "wifi_status"
