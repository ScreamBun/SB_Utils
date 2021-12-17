"""
Local Cache for ETCd values
"""
import copy
import json
import re
import etcd3

from threading import Lock
from typing import Callable, List, Tuple, Union
from etcd3.events import Event, DeleteEvent, PutEvent
from etcd3.watch import WatchResponse
from .general import isFunction
from .ext_dicts import FrozenDict, QueryDict


# Type Hinting
Callback = Callable[[FrozenDict], None]
Callbacks = Union[
    List[Callback],
    Tuple[Callback, ...]
]


class EtcdCache:
    _callbacks: List[Callback]
    _data: QueryDict
    _etcd_client: etcd3.client
    _lock: Lock
    _root: str
    _watcher_id: int

    def __init__(self, host: str, port: int, base: str, callbacks: Callbacks = None):
        self._callbacks = []
        if isinstance(callbacks, (list, tuple)):
            self._callbacks.extend([f for f in callbacks if isFunction(f)])

        self._root = base if base.startswith('/') else f'/{base}'
        self._root = self._root[:-1] if self._root.endswith('/') else self._root
        self._etcd_client = etcd3.client(
            host=host,
            port=port
        )
        self._lock = Lock()
        self._data = self._init_data()
        self._watcher_id = self._etcd_client.add_watch_prefix_callback(key_prefix=self._root, callback=self._update)

    @property
    def cache(self) -> FrozenDict:
        with self._lock:
            return FrozenDict(self._data)

    def shutdown(self) -> None:
        self._etcd_client.cancel_watch(self._watcher_id)

    # Dict-like
    def get(self, key: str) -> FrozenDict:
        with self._lock:
            return FrozenDict(self._data.get(key, {}))

    # Helper Methods
    def _init_data(self, base: str = None) -> QueryDict:
        """
        Get ETCD initial values
        """
        root = base or self._root
        data = QueryDict()
        for val, meta in self._etcd_client.get_prefix(root):
            key = re.sub(fr'^{root}/'.encode(), b'', meta.key).decode().replace('/', '.')
            data[key] = json.loads(val)
        return data

    def _update(self, response: WatchResponse) -> None:
        events: List[Event] = response.events
        for evt in events:
            key = re.sub(fr'^{self._root}/'.encode(), b'', evt.key).decode().replace('/', '.')
            with self._lock:
                tmp = copy.deepcopy(self._data)
            if isinstance(evt, PutEvent):
                val = json.loads(evt.value)
                with self._lock:
                    self._data[key] = val
            elif isinstance(evt, DeleteEvent):
                with self._lock:
                    del self._data[key]
            else:
                print(f"Unknown Event - {evt}", flush=True)

            with self._lock:
                if tmp != self._data:
                    for func in self._callbacks:
                        func(self.cache)
