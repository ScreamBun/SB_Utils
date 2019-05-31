from typing import Any, List, Type


class FrozenDict(dict):
    """
    Immutible dictonary
    """

    def __init__(self, *args, **kwargs) -> None:
        self._hash = None
        super(FrozenDict, self).__init__(*args, **kwargs)

    def __hash__(self) -> int:
        if self._hash is None:
            self._hash = hash(tuple(sorted(self.items())))  # iteritems() on py2
        return self._hash

    def __getattr__(self, item: str) -> Any:
        return self.get(item, None)

    def __getitem__(self, item: str) -> Any:
        return self.get(item, None)

    def _immutable(self, *args, **kws):
        raise TypeError('cannot change object - object is immutable')

    __setitem__ = _immutable
    __delitem__ = _immutable
    pop = _immutable
    popitem = _immutable
    clear = _immutable
    update = _immutable
    setdefault = _immutable


class MultiKeyDict(dict):
    """
    Multi Key traversal dictionary
    d = MultiKeyDict()

    d['192']['168']['1']['100'] = 'test.domain.local'
        SAME AS
    d['192.168.1.100'] = 'test.domain.local'
    """

    def __init__(self, sep: str = '.', *args, **kwargs) -> None:
        super(MultiKeyDict, self).__init__(*args, **kwargs)
        self._sep = sep

        for k, v in dict(self).items():
            if self._sep in k:
                dict.__delitem__(self, k)
                keys = self._keySplit(k)
                dict.setdefault(self, keys[0], MultiKeyDict(sep=self._sep))[self._sep.join(keys[1:])] = v

    def __setitem__(self, key: str, val: Any) -> None:
        keys = self._keySplit(key)
        if len(keys) == 1:
            dict.__setitem__(self, key, val)
        else:
            self[keys[0]] = MultiKeyDict(
                sep=self._sep,
                **{
                    **dict.get(self, keys[0], {}),
                    self._sep.join(keys[1:]): val,
                }
            )

    def __getitem__(self, key: str) -> Any:
        keys = self._keySplit(key)
        if len(keys) == 1:
            return dict.__getitem__(self, key)
        else:
            rtn = self
            for key in keys:
                rtn = dict.get(rtn, key, None)
            return rtn

    def __delitem__(self, key: str) -> None:
        keys = self._keySplit(key)
        if len(keys) == 1:
            dict.__delitem__(self, key)
        else:
            k = dict.get(self, keys[0], None)
            if k:
                k.__delitem__(self._sep.join(keys[1:]))

    def __contains__(self, item) -> bool:
        keys = self._keySplit(item)
        return item in self._compositKeys(self) if len(keys) > 1 else dict.get(self, item, None) is not None

    def get(self, key: str, default: Any = None) -> Any:
        return self[key] if key in self else default

    def compositKeys(self) -> List[str]:
        return self._compositKeys(self)

    # helper functions
    def _compositKeys(self, obj: dict) -> List[str]:
        if isinstance(obj, self.__class__):
            tmp = []
            for key, val in obj.items():
                val_keys = self._compositKeys(val)
                if len(val_keys) > 0:
                    tmp.extend([f"{key}{self._sep}{k}" for k in val_keys])
                else:
                    tmp.append(key)
            return tmp
        else:
            return []

    def _keySplit(self, k):
        return list(filter(None, k.split(self._sep)))


class ObjectDict(dict):
    """
    Dictionary thats acts like a mutable object
    d = ObjectDict()

    d['key'] = 'value'
        SAME AS
    d.key = 'value'
    """

    def __init__(self, *args, **kwargs):
        self._hash = None
        super(ObjectDict, self).__init__(*args, **kwargs)

    def __getattr__(self, item: str) -> Any:
        return self.get(item, None)

    def __setitem__(self, key: str, val: Any) -> None:
        dict.__setitem__(self, key, val)
