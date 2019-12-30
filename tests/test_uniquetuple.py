from typing import Sequence, Hashable, Union

from hypothesis import given, infer

from collectionish import uniquetuple
from collectionish.types import UniqueTuple

from tests.utils import param, mark_params


@given(args=infer)
def test_uniquetuple_is_unique(args: Sequence[Hashable]):
    assert len(uniquetuple(*args)) == len(set(args))


@mark_params
@param(tag='ordering', inp=(3, 3, 2, 3, 2, 1, 2, 3), expected=uniquetuple(3, 2, 1))
@param(tag='empty', inp=[], expected=uniquetuple())
def test_explicit_examples(inp, expected):
    assert uniquetuple(*inp) == expected


@mark_params
@param(inp=int)
@param(inp=str)
@param(inp=Union[int, str])
def test_typehints(inp):
    hint = UniqueTuple[inp]
    assert hint.__args__ == (inp,)
    assert hint.__origin__ == uniquetuple
