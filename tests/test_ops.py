from typing import NamedTuple, Any, Iterator, Tuple, Dict


import string
from types import SimpleNamespace

import pytest

import hypothesis.strategies as st
from hypothesis import given

from collectionish import AttyDict
from collectionish.utils import is_valid_identifier, is_mapping
from collectionish.ops import rgetattr, flatten_mapping

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


def test_flatten_attydict_with_keeptype_and_dot_delim_raises_error():
    attydict = AttyDict(this={'nested': {'number': 1, 'name': 'teddy'}}, other=2)
    expect_msg = (
        'cannot use dot delimiter with AttyDict'
        ' try specifying a different delimiter such as an underscore'
        ' or set keep_type to False to return a regular dict.'
    )
    with pytest.raises(TypeError, match=expect_msg):
        flatten_mapping(attydict, keep_type=True)


def test_flatten_attydict_with_keeptype_and_underscore_delim_is_fine():
    attydict = AttyDict(this={'nested': {'number': 1, 'name': 'teddy'}}, other=2)
    flat = flatten_mapping(attydict, keep_type=True, delimiter='_')
    assert isinstance(flat, AttyDict)
    assert flat == AttyDict(this_nested_number=1, this_nested_name='teddy', other=2)
