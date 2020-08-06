from enum import Enum


class Serializations(Enum):
    """
    The content format of an OpenC2 Message
    """
    Binn = 'binn'
    Bencode = 'bencode'
    BSON = 'bson'
    CBOR = 'cbor'
    JSON = 'json'
    MsgPack = 'msgpack'
    S_Expression = 's_expression'
    # Smile = 'smile'
    TOML = 'toml'
    XML = 'xml'
    UBJSON = 'ubjson'
    YAML = 'yaml'
    VPack = 'vpack'
