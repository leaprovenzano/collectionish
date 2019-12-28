from typing import Union

from more_containers.types import AttyDict

from tests.utils import param, mark_params


@mark_params
@param(inp=int)
@param(inp=str)
@param(inp=Union[int, str])
def test_typehints(inp):
    hint = AttyDict[inp]
    assert hint.__args__ == (inp,)
    assert hint.__origin__ == AttyDict
