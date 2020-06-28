import pytest
from collections import ChainMap
from collectionish import AncestorChainMap


@pytest.mark.parametrize(
    'parent,', [{'a': 1, 'b': 2}, ChainMap({'a': 1, 'b': 2}), AncestorChainMap({'a': 1, 'b': 2})]
)
def test_add_parent(parent):
    child = AncestorChainMap({'b': 3, 'c': 4})
    child.add_parent(parent)
    assert dict(child) == {'a': 1, 'b': 3, 'c': 4}


@pytest.mark.parametrize(
    'ancestor,', [{'a': 1, 'd': 1}, ChainMap({'a': 1, 'd': 1}), AncestorChainMap({'a': 1, 'd': 1})]
)
def test_add_ancestor(ancestor):
    child = AncestorChainMap({'b': 3, 'c': 3}, {'a': 2, 'b': 2})
    child.add_ancestor(ancestor)
    assert dict(child) == {'a': 2, 'b': 3, 'c': 3, 'd': 1}
