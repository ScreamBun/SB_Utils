from enum import Enum


class SerialFormats(Enum):
    """
    The type of an OpenC2 Serialization
    """
    BINN = 1
    BENCODE = 2
    BSON = 3
    CBOR = 4
    JSON = 5
    MSGPACK = 6
    S_EXPRESSION = 7
    SMILE = 8
    TOML = 9
    XML = 10
    UBJSON = 11
    VPACK = 12
    YAML = 13
