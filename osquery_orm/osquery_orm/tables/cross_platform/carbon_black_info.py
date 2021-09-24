"""
OSQuery carbon_black_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class CarbonBlackInfo(BaseModel):
    """
    Returns info about a Carbon Black sensor install.
    """
    # Sensor ID of the Carbon Black sensor
    sensor_id = IntegerField()
    # Sensor group
    config_name = TextField()
    # If the sensor is configured to send back binaries to the Carbon Black server
    collect_store_files = IntegerField()
    # If the sensor is configured to capture module loads
    collect_module_loads = IntegerField()
    # If the sensor is configured to collect metadata of binaries
    collect_module_info = IntegerField()
    # If the sensor is configured to collect file modification events
    collect_file_mods = IntegerField()
    # If the sensor is configured to collect registry modification events
    collect_reg_mods = IntegerField()
    # If the sensor is configured to collect network connections
    collect_net_conns = IntegerField()
    # If the sensor is configured to process events
    collect_processes = IntegerField()
    # If the sensor is configured to cross process events
    collect_cross_processes = IntegerField()
    # If the sensor is configured to EMET events
    collect_emet_events = IntegerField()
    # If the sensor is configured to collect non binary file writes
    collect_data_file_writes = IntegerField()
    # If the sensor is configured to collect the user running a process
    collect_process_user_context = IntegerField()
    # Unknown
    collect_sensor_operations = IntegerField()
    # Event file disk quota in MB
    log_file_disk_quota_mb = IntegerField()
    # Event file disk quota in a percentage
    log_file_disk_quota_percentage = IntegerField()
    # If the sensor is configured to report tamper events
    protection_disabled = IntegerField()
    # IP address of the sensor
    sensor_ip_addr = TextField()
    # Carbon Black server
    sensor_backend_server = TextField()
    # Size in bytes of Carbon Black event files on disk
    event_queue = IntegerField()
    # Size in bytes of binaries waiting to be sent to Carbon Black server
    binary_queue = IntegerField()

    class Meta:
        table_name = "carbon_black_info"
