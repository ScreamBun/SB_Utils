"""
OSQuery launchd ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class Launchd(BaseModel):
    """
    LaunchAgents and LaunchDaemons from default search paths.
    """
    # Path to daemon or agent plist
    path = TextField()  # {'index': True}
    # File name of plist (used by launchd)
    name = TextField()
    # Daemon or agent service name
    label = TextField()
    # Path to target program
    program = TextField()
    # Should the program run on launch load
    run_at_load = TextField()
    # Should the process be restarted if killed
    keep_alive = TextField()
    # Deprecated key, replaced by keep_alive
    on_demand = TextField()
    # Skip loading this daemon or agent on boot
    disabled = TextField()
    # Run this daemon or agent as this username
    username = TextField()
    # Run this daemon or agent as this group
    groupname = TextField()
    # Pipe stdout to a target path
    stdout_path = TextField()
    # Pipe stderr to a target path
    stderr_path = TextField()
    # Frequency to run in seconds
    start_interval = TextField()
    # Command line arguments passed to program
    program_arguments = TextField()
    # Key that launches daemon or agent if path is modified
    watch_paths = TextField()
    # Similar to watch_paths but only with non-empty directories
    queue_directories = TextField()
    # Run this daemon or agent as it was launched from inetd
    inetd_compatibility = TextField()
    # Run daemon or agent every time a filesystem is mounted
    start_on_mount = TextField()
    # Key used to specify a directory to chroot to before launch
    root_directory = TextField()
    # Key used to specify a directory to chdir to before launch
    working_directory = TextField()
    # Key describes the intended purpose of the job
    process_type = TextField()

    class Meta:
        table_name = "launchd"
