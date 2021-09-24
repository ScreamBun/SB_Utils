"""
OSQuery lldp_neighbors ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class LldpNeighbors(BaseModel):
    """
    LLDP neighbors of interfaces.
    """
    # Interface name
    interface = TextField()
    # Neighbor chassis index
    rid = IntegerField()
    # Neighbor chassis ID type
    chassis_id_type = TextField()
    # Neighbor chassis ID value
    chassis_id = TextField()
    # CPU brand string, contains vendor and model
    chassis_sysname = TextField()
    # Max number of CPU physical cores
    chassis_sys_description = IntegerField()
    # Chassis bridge capability availability
    chassis_bridge_capability_available = IntegerField()
    # Is chassis bridge capability enabled.
    chassis_bridge_capability_enabled = IntegerField()
    # Chassis router capability availability
    chassis_router_capability_available = IntegerField()
    # Chassis router capability enabled
    chassis_router_capability_enabled = IntegerField()
    # Chassis repeater capability availability
    chassis_repeater_capability_available = IntegerField()
    # Chassis repeater capability enabled
    chassis_repeater_capability_enabled = IntegerField()
    # Chassis wlan capability availability
    chassis_wlan_capability_available = IntegerField()
    # Chassis wlan capability enabled
    chassis_wlan_capability_enabled = IntegerField()
    # Chassis telephone capability availability
    chassis_tel_capability_available = IntegerField()
    # Chassis telephone capability enabled
    chassis_tel_capability_enabled = IntegerField()
    # Chassis DOCSIS capability availability
    chassis_docsis_capability_available = IntegerField()
    # Chassis DOCSIS capability enabled
    chassis_docsis_capability_enabled = IntegerField()
    # Chassis station capability availability
    chassis_station_capability_available = IntegerField()
    # Chassis station capability enabled
    chassis_station_capability_enabled = IntegerField()
    # Chassis other capability availability
    chassis_other_capability_available = IntegerField()
    # Chassis other capability enabled
    chassis_other_capability_enabled = IntegerField()
    # Comma delimited list of chassis management IPS
    chassis_mgmt_ips = TextField()
    # Port ID type
    port_id_type = TextField()
    # Port ID value
    port_id = TextField()
    # Port description
    port_description = TextField()
    # Age of neighbor port
    port_ttl = BigIntegerField()
    # Port max frame size
    port_mfs = BigIntegerField()
    # Port aggregation ID
    port_aggregation_id = TextField()
    # Auto negotiation supported
    port_autoneg_supported = IntegerField()
    # Is auto negotiation enabled
    port_autoneg_enabled = IntegerField()
    # MAU type
    port_mau_type = TextField()
    # 10Base-T HD auto negotiation enabled
    port_autoneg_10baset_hd_enabled = IntegerField()
    # 10Base-T FD auto negotiation enabled
    port_autoneg_10baset_fd_enabled = IntegerField()
    # 100Base-TX HD auto negotiation enabled
    port_autoneg_100basetx_hd_enabled = IntegerField()
    # 100Base-TX FD auto negotiation enabled
    port_autoneg_100basetx_fd_enabled = IntegerField()
    # 100Base-T2 HD auto negotiation enabled
    port_autoneg_100baset2_hd_enabled = IntegerField()
    # 100Base-T2 FD auto negotiation enabled
    port_autoneg_100baset2_fd_enabled = IntegerField()
    # 100Base-T4 HD auto negotiation enabled
    port_autoneg_100baset4_hd_enabled = IntegerField()
    # 100Base-T4 FD auto negotiation enabled
    port_autoneg_100baset4_fd_enabled = IntegerField()
    # 1000Base-X HD auto negotiation enabled
    port_autoneg_1000basex_hd_enabled = IntegerField()
    # 1000Base-X FD auto negotiation enabled
    port_autoneg_1000basex_fd_enabled = IntegerField()
    # 1000Base-T HD auto negotiation enabled
    port_autoneg_1000baset_hd_enabled = IntegerField()
    # 1000Base-T FD auto negotiation enabled
    port_autoneg_1000baset_fd_enabled = IntegerField()
    # Dot3 power device type
    power_device_type = TextField()
    # MDI power supported
    power_mdi_supported = IntegerField()
    # Is MDI power enabled
    power_mdi_enabled = IntegerField()
    # Is power pair control enabled
    power_paircontrol_enabled = IntegerField()
    # Dot3 power pairs
    power_pairs = TextField()
    # Power class
    power_class = TextField()
    # Is 802.3at enabled
    power_8023at_enabled = IntegerField()
    # 802.3at power type
    power_8023at_power_type = TextField()
    # 802.3at power source
    power_8023at_power_source = TextField()
    # 802.3at power priority
    power_8023at_power_priority = TextField()
    # 802.3at power allocated
    power_8023at_power_allocated = TextField()
    # 802.3at power requested
    power_8023at_power_requested = TextField()
    # Chassis MED type
    med_device_type = TextField()
    # Is MED capabilities enabled
    med_capability_capabilities = IntegerField()
    # Is MED policy capability enabled
    med_capability_policy = IntegerField()
    # Is MED location capability enabled
    med_capability_location = IntegerField()
    # Is MED MDI PSE capability enabled
    med_capability_mdi_pse = IntegerField()
    # Is MED MDI PD capability enabled
    med_capability_mdi_pd = IntegerField()
    # Is MED inventory capability enabled
    med_capability_inventory = IntegerField()
    # Comma delimited list of MED policies
    med_policies = TextField()
    # Comma delimited list of vlan ids
    vlans = TextField()
    # Primary VLAN id
    pvid = TextField()
    # Comma delimited list of supported PPVIDs
    ppvids_supported = TextField()
    # Comma delimited list of enabled PPVIDs
    ppvids_enabled = TextField()
    # Comma delimited list of PIDs
    pids = TextField()

    class Meta:
        table_name = "lldp_neighbors"
