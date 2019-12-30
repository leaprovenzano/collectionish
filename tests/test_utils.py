import typing as t
import ast
from types import MappingProxyType

import hypothesis.strategies as st
from hypothesis import given

from collectionish.utils import is_valid_identifier
from collectionish.utils import is_mapping, is_arraylike

from tests.utils import param, mark_params
from tests.strategies import everything_except, one_of_types

MAPPING_TYPES = (t.Mapping, t.MutableMapping, dict)


def validate_identifier_as_ast(s: str):
    parsed = ast.parse(f'{s}=1', mode='single')
    assert len(parsed.body) == 1
    body = parsed.body[0]
    assert isinstance(body, ast.Assign)
    assert body.lineno == 1
    assert body.col_offset == 0

    assert body.value.n == 1

    assert len(body.targets) == 1
    name = body.targets[0]
    assert isinstance(name, ast.Name)
    assert name.id == s


@given(st.text())
def test_is_valid_identifier(s):
    if is_valid_identifier(s):
        validate_identifier_as_ast(s)


@mark_params
@param(obj=one_of_types(*MAPPING_TYPES) | st.from_type(dict).map(MappingProxyType), expected=True)
@param(obj=everything_except(*MAPPING_TYPES, MappingProxyType), expected=False)
@given(data=st.data())
def test_is_mapping(data, obj, expected):
    inp = data.draw(obj)
    assert is_mapping(inp) == expected


@mark_params
@param(obj=one_of_types(list, tuple, frozenset, set), expected=True)
@param(obj=everything_except(list, tuple, frozenset, set), expected=False)
@given(data=st.data())
def test_is_arraylike(data, obj, expected):
    inp = data.draw(obj)
    assert is_arraylike(inp) == expected
