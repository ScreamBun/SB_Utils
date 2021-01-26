from enum import Enum, EnumMeta
from typing import Union


class EnumMetaSB(EnumMeta):
    def __contains__(cls, item):
        return item in list(cls.__members__.values())


class EnumBase(Enum, metaclass=EnumMetaSB):
    @classmethod
    def from_name(cls, fmt: str):
        name = fmt.upper()
        for k, v in dict(cls.__members__).items():
            if name == k.upper():
                return cls.__getattr__(k)
        raise ValueError(f'{name} is not a valid format name')

    @classmethod
    def from_value(cls, fmt: Union[int, str]):
        members = dict(cls.__members__)
        for k, v in members.items():
            if fmt == v:
                return cls.__getattr__(k)
        raise ValueError(f'{fmt} is not a valid format value')
