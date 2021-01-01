import pytest
from copy import deepcopy
from collectionish import NumDict, AttyNumDict


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), AttyNumDict(a=1.54, b=2.1)])
def test_scalar_addition(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v + 2 for k, v in x.items()})
    y = x + 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), AttyNumDict(a=1.54, b=2.1)])
def test_scalar_subtraction(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v - 2 for k, v in x.items()})
    y = x - 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), AttyNumDict(a=1.54, b=2.1)])
def test_scalar_multiplication(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v * 2 for k, v in x.items()})
    y = x * 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), AttyNumDict(a=1.54, b=2.1)])
def test_scalar_division(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v / 2 for k, v in x.items()})
    y = x / 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), AttyNumDict(a=1.54, b=2.1)])
def test_scalar_exponentiation(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v ** 2 for k, v in x.items()})
    y = x ** 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), AttyNumDict(a=1.54, b=2.1)])
def test_scalar_floor_division(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v // 2 for k, v in x.items()})
    y = x // 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), AttyNumDict(a=1.54, b=2.1)])
def test_scalar_modulus(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v % 2 for k, v in x.items()})
    y = x % 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig
