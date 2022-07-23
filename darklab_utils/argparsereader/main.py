import argparse
from copy import deepcopy, copy
from types import SimpleNamespace


class _SimpleNameSpaceWithDict(SimpleNamespace):
    """for typing / documentation purposes exposed to user"""
    def get_as_dict() -> dict:
        pass

class ArgparseWithAugmentedArgs(argparse.ArgumentParser):
    def parse_args(self, ignore_others: bool, args: list[str], **kwargs) -> _SimpleNameSpaceWithDict:

        if ignore_others:
            args, *_ = super().parse_known_args(args, **kwargs)
        else:
            args = super().parse_args(args, **kwargs)

        def get_as_dict() -> dict:
            data = copy(args.__dict__)
            if "get_as_dict" in data:
                data.pop("get_as_dict")
            return data

        args.get_as_dict = get_as_dict
        return args

class ArgparseReader:
    def __init__(self):
        self._parser = ArgparseWithAugmentedArgs()

    def add_argument(self, *args, **kwargs) -> 'ArgparseReader':
        copy_of_self = deepcopy(self)
        copy_of_self._parser.add_argument(*args, **kwargs)
        return copy_of_self

    def get_data(self, ignore_others: bool = False, args: list[str] = None) -> _SimpleNameSpaceWithDict:
        args = self._parser.parse_args(ignore_others=ignore_others, args=args)
        return args