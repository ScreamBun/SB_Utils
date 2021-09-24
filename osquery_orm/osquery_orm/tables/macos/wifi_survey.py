"""
OSQuery wifi_survey ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class WifiSurvey(BaseModel):
    """
    Scan for nearby WiFi networks.
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

    class Meta:
        table_name = "wifi_survey"
