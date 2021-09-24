"""
Table Constants
"""
from enum import Enum


class Compatibility(str, Enum):
    MacOS = "macos"
    FreeBSD = "freebsd"
    Linux = "linux"
    Windows = "windows"
