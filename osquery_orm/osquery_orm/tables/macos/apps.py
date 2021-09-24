"""
OSQuery apps ORM
"""
from osquery_orm.orm import BaseModel
from peewee import DoubleField, TextField


class Apps(BaseModel):
    """
    OS X applications installed in known search paths (e.g., /Applications).
    """
    # Name of the Name.app folder
    name = TextField()
    # Absolute and full Name.app path
    path = TextField()  # {'index': True}
    # Info properties CFBundleExecutable label
    bundle_executable = TextField()
    # Info properties CFBundleIdentifier label
    bundle_identifier = TextField()
    # Info properties CFBundleName label
    bundle_name = TextField()
    # Info properties CFBundleShortVersionString label
    bundle_short_version = TextField()
    # Info properties CFBundleVersion label
    bundle_version = TextField()
    # Info properties CFBundlePackageType label
    bundle_package_type = TextField()
    # Application-set environment variables
    environment = TextField()
    # Does the app identify as a background agent
    element = TextField()
    # Info properties DTCompiler label
    compiler = TextField()
    # Info properties CFBundleDevelopmentRegion label
    development_region = TextField()
    # Info properties CFBundleDisplayName label
    display_name = TextField()
    # Info properties CFBundleGetInfoString label
    info_string = TextField()
    # Minimum version of OS X required for the app to run
    minimum_system_version = TextField()
    # The UTI that categorizes the app for the App Store
    category = TextField()
    # Info properties NSAppleScriptEnabled label
    applescript_enabled = TextField()
    # Info properties NSHumanReadableCopyright label
    copyright = TextField()
    # The time that the app was last used
    last_opened_time = DoubleField()

    class Meta:
        table_name = "apps"
