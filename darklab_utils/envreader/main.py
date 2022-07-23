from types import SimpleNamespace
from copy import deepcopy
import os

class EnvReader:
    def __init__(self):
        self._storage = SimpleNamespace()

    def __getitem__(self, key) -> str:
        return os.environ[key]

    def get(self, key, default = None) -> str:
        return os.environ.get(key, default)

    def add_arguments(self, **kwargs) -> 'EnvReader':
        self = deepcopy(self)
        for key, value in kwargs.items():
            setattr(self._storage, key, value)
        return self

    def get_storage(self) -> 'SimpleNamespace':
        return self._storage
