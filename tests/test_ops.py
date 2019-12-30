from typing import NamedTuple, Any, Iterator, Tuple, Dict


import string
from types import SimpleNamespace

import pytest

import hypothesis.strategies as st
from hypothesis import given

from collectionish.utils import is_valid_identifier
from collectionish.utils import is_mapping


from collectionish.ops import rgetattr

py_names = st.text(string.ascii_lowercase + '_').filter(is_valid_identifier)


class Pair(NamedTuple):

    path: Tuple[str]
    value: Any


class Thing(SimpleNamespace):

    @classmethod
    def from_dict(cls, dct: Dict[str, Any]) -> 'Thing':
        kwargs = {}
        for k, v in dct.items():
            if is_mapping(v):
                kwargs[k] = cls.from_dict(v)
            else:
                kwargs[k] = v
        return cls(**kwargs)

    def paths(self, prefix=tuple([])) -> Iterator[Pair]:
        yield Pair(prefix, self)
        for k, v in self.__dict__.items():
            if isinstance(v, self.__class__):
                for path, v in v.paths(prefix + (k,)):
                    yield Pair(path, v)
            else:
                yield Pair(prefix + (k,), v)


things = st.builds(
    Thing.from_dict, st.dictionaries(keys=py_names, values=st.text(string.ascii_lowercase))
)


@given(things)
def test_rgetattr(thing):
    for path, value in thing.paths():
        assert rgetattr(thing, *path) == value


@given(things, st.data())
def test_rgetattr_raises_on_invalid(thing, data):
    path, _ = data.draw(st.sampled_from(list(thing.paths())))
    with pytest.raises(AttributeError):
        rgetattr(thing, *path, 'bullshit')
