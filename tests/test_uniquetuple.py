from typing import Sequence, Hashable, Union

from hypothesis import given, infer, assume

from collectionish import UniqueTuple
from collectionish.utils import is_hashable

from tests.utils import param, mark_params


@given(args=infer)
def test_uniquetuple_is_unique(args: Sequence[Hashable]):
    assume(all(map(is_hashable, args)))
    assert len(UniqueTuple(*args)) == len(set(args))


@mark_params
@param(tag='ordering', inp=(3, 3, 2, 3, 2, 1, 2, 3), expected=UniqueTuple(3, 2, 1))
@param(tag='empty', inp=[], expected=UniqueTuple())
def test_explicit_examples(inp, expected):
    assert UniqueTuple(*inp) == expected


@mark_params
@param(inp=int)
@param(inp=str)
@param(inp=Union[int, str])
def test_typehints(inp):
    hint = UniqueTuple[inp]
    assert hint.__args__ == (inp,)
    assert hint.__origin__ == UniqueTuple
