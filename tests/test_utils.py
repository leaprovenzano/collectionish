import ast

import pytest

import hypothesis.strategies as st
from hypothesis import given

from more_containers.utils import is_valid_identifier


@given(st.text())
def test_is_valid_identifier(s):
    statement = f'{s}=1'
    if is_valid_identifier(s):
        ast.literal_eval(statement)
    else:
        with pytest.raises(SyntaxError):
            ast.literal_eval(statement)
