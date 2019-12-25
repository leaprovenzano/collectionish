import ast

import hypothesis.strategies as st
from hypothesis import given

from more_containers.utils import is_valid_identifier


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
