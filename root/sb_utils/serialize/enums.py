from ..utils import EnumBase


class SerialFormats(str, EnumBase):
    """
    The format of an OpenC2 Serialization
    """
    # Binary Format
    BINN = 'binn'
    BSON = 'bson'
    CBOR = 'cbor'
    MSGPACK = 'msgpack'
    SMILE = 'smile'
    # VPACK = 'vpack'
    # Text Format
    BENCODE = 'bencode'
    JSON = 'json'
    S_EXPRESSION = 'sexp'
    TOML = 'toml'
    UBJSON = 'ubjson'
    XML = 'xml'
    YAML = 'yaml'

    @classmethod
    def is_binary(cls, fmt: 'SerialFormats') -> bool:
        """
        Determine if the format is binary or text based
        :param fmt: Serialization
        """
        return fmt in (cls.BINN, cls.BSON, cls.CBOR, cls.MSGPACK, cls.SMILE)
