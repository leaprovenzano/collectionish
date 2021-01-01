import pytest
from copy import deepcopy
from collectionish import NumDict, NumAttyDict


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), NumAttyDict(a=1.54, b=2.1)])
def test_scalar_addition(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v + 2 for k, v in x.items()})
    y = x + 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), NumAttyDict(a=1.54, b=2.1)])
def test_scalar_subtraction(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v - 2 for k, v in x.items()})
    y = x - 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), NumAttyDict(a=1.54, b=2.1)])
def test_scalar_multiplication(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v * 2 for k, v in x.items()})
    y = x * 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), NumAttyDict(a=1.54, b=2.1)])
def test_scalar_division(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v / 2 for k, v in x.items()})
    y = x / 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), NumAttyDict(a=1.54, b=2.1)])
def test_scalar_power(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v ** 2 for k, v in x.items()})
    y = x ** 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), NumAttyDict(a=1.54, b=2.1)])
def test_scalar_floor_division(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v // 2 for k, v in x.items()})
    y = x // 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), NumAttyDict(a=1.54, b=2.1)])
def test_scalar_modulus(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v % 2 for k, v in x.items()})
    y = x % 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig

    @pytest.mark.parametrize('x,', [NumDict(a=3, b=2), NumAttyDict(a=3, b=2)])
    def test_rightand_scalar_addition(x):
        orig = deepcopy(x)
        expected = x.__class__({k: 23.256 + v for k, v in x.items()})
        y = 23.256 + x
        assert y == expected
        assert isinstance(y, x.__class__)
        assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=3, b=2), NumAttyDict(a=3, b=2)])
def test_rightand_scalar_subtraction(x):
    orig = deepcopy(x)
    expected = x.__class__({k: 23.256 - v for k, v in x.items()})
    y = 23.256 - x
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=3, b=2), NumAttyDict(a=3, b=2)])
def test_rightand_scalar_multiplication(x):
    orig = deepcopy(x)
    expected = x.__class__({k: 23.256 * v for k, v in x.items()})
    y = 23.256 * x
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=3, b=2), NumAttyDict(a=3, b=2)])
def test_rightand_scalar_division(x):
    orig = deepcopy(x)
    expected = x.__class__({k: 23.256 / v for k, v in x.items()})
    y = 23.256 / x
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=3, b=2), NumAttyDict(a=3, b=2)])
def test_rightand_scalar_power(x):
    orig = deepcopy(x)
    expected = x.__class__({k: 23.256 ** v for k, v in x.items()})
    y = 23.256 ** x
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=3, b=2), NumAttyDict(a=3, b=2)])
def test_rightand_scalar_floor_division(x):
    orig = deepcopy(x)
    expected = x.__class__({k: 23.256 // v for k, v in x.items()})
    y = 23.256 // x
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=3, b=2), NumAttyDict(a=3, b=2)])
def test_rightand_scalar_modulus(x):
    orig = deepcopy(x)
    expected = x.__class__({k: 23.256 % v for k, v in x.items()})
    y = 23.256 % x
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize('x,', [NumDict(a=3.5, b=2.24), NumAttyDict(a=3.5, b=2.24)])
def test_inplace_scalar_addition(x):
    expected = x.__class__({k: v + 2 for k, v in x.items()})
    x += 2
    assert x == expected


@pytest.mark.parametrize('x,', [NumDict(a=3.5, b=2.24), NumAttyDict(a=3.5, b=2.24)])
def test_inplace_scalar_subtraction(x):
    expected = x.__class__({k: v - 2 for k, v in x.items()})
    x -= 2
    assert x == expected


@pytest.mark.parametrize('x,', [NumDict(a=3.5, b=2.24), NumAttyDict(a=3.5, b=2.24)])
def test_inplace_scalar_multiplication(x):
    expected = x.__class__({k: v * 2 for k, v in x.items()})
    x *= 2
    assert x == expected


@pytest.mark.parametrize('x,', [NumDict(a=3.5, b=2.24), NumAttyDict(a=3.5, b=2.24)])
def test_inplace_scalar_division(x):
    expected = x.__class__({k: v / 2 for k, v in x.items()})
    x /= 2
    assert x == expected


@pytest.mark.parametrize('x,', [NumDict(a=3.5, b=2.24), NumAttyDict(a=3.5, b=2.24)])
def test_inplace_scalar_power(x):
    expected = x.__class__({k: v ** 2 for k, v in x.items()})
    x **= 2
    assert x == expected


@pytest.mark.parametrize('x,', [NumDict(a=3.5, b=2.24), NumAttyDict(a=3.5, b=2.24)])
def test_inplace_scalar_floor_division(x):
    expected = x.__class__({k: v // 2 for k, v in x.items()})
    x //= 2
    assert x == expected


@pytest.mark.parametrize('x,', [NumDict(a=3.5, b=2.24), NumAttyDict(a=3.5, b=2.24)])
def test_inplace_scalar_modulus(x):
    expected = x.__class__({k: v % 2 for k, v in x.items()})
    x %= 2
    assert x == expected


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumDict(a=5.54, b=7.5)),
        (NumDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumDict(a=5.54, b=7.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3, extra=4), NumDict(a=5.54, b=7.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2), NumDict(a=5.54, b=4.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumAttyDict(a=5.54, b=7.5)),
        (NumAttyDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumAttyDict(a=5.54, b=7.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=5.54, b=7.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2), NumAttyDict(a=5.54, b=4.5)),
    ],
)
def test_oop_addition_with_other(x, y, expected):
    orig_x = deepcopy(x)
    orig_y = deepcopy(y)

    assert x + y == expected
    assert x == orig_x
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3, extra=4), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2), NumDict(a=1.54, b=4.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2), NumAttyDict(a=1.54, b=4.5)),
    ],
)
def test_oop_subtraction_with_other(x, y, expected):
    orig_x = deepcopy(x)
    orig_y = deepcopy(y)

    assert x - y == expected
    assert x == orig_x
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumDict(a=7.08, b=13.5)),
        (NumDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumDict(a=7.08, b=13.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3, extra=4), NumDict(a=7.08, b=13.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2), NumDict(a=7.08, b=4.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumAttyDict(a=7.08, b=13.5)),
        (NumAttyDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumAttyDict(a=7.08, b=13.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=7.08, b=13.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2), NumAttyDict(a=7.08, b=4.5)),
    ],
)
def test_oop_multiplication_with_other(x, y, expected):
    orig_x = deepcopy(x)
    orig_y = deepcopy(y)

    assert x * y == expected
    assert x == orig_x
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumDict(a=1.77, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumDict(a=1.77, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3, extra=4), NumDict(a=1.77, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2), NumDict(a=1.77, b=4.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumAttyDict(a=1.77, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumAttyDict(a=1.77, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=1.77, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2), NumAttyDict(a=1.77, b=4.5)),
    ],
)
def test_oop_division_with_other(x, y, expected):
    orig_x = deepcopy(x)
    orig_y = deepcopy(y)

    assert x / y == expected
    assert x == orig_x
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3, b=4), NumDict(a=2, b=3), NumDict(a=9, b=64)),
        (NumDict(a=3, b=4), NumAttyDict(a=2, b=3), NumDict(a=9, b=64)),
        (NumDict(a=3, b=4), NumDict(a=2, b=3, extra=4), NumDict(a=9, b=64)),
        (NumDict(a=3, b=4), NumDict(a=2), NumDict(a=9, b=4)),
        (NumAttyDict(a=3, b=4), NumAttyDict(a=2, b=3), NumAttyDict(a=9, b=64)),
        (NumAttyDict(a=3, b=4), NumDict(a=2, b=3), NumAttyDict(a=9, b=64)),
        (NumAttyDict(a=3, b=4), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=9, b=64)),
        (NumAttyDict(a=3, b=4), NumAttyDict(a=2), NumAttyDict(a=9, b=4)),
    ],
)
def test_oop_power_with_other(x, y, expected):
    orig_x = deepcopy(x)
    orig_y = deepcopy(y)

    assert x ** y == expected
    assert x == orig_x
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=39, b=45), NumDict(a=2, b=3), NumDict(a=19, b=15)),
        (NumDict(a=39, b=45), NumAttyDict(a=2, b=3), NumDict(a=19, b=15)),
        (NumDict(a=39, b=45), NumDict(a=2, b=3, extra=4), NumDict(a=19, b=15)),
        (NumDict(a=39, b=45), NumDict(a=2), NumDict(a=19, b=45)),
        (NumAttyDict(a=39, b=45), NumAttyDict(a=2, b=3), NumAttyDict(a=19, b=15)),
        (NumAttyDict(a=39, b=45), NumDict(a=2, b=3), NumAttyDict(a=19, b=15)),
        (NumAttyDict(a=39, b=45), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=19, b=15)),
        (NumAttyDict(a=39, b=45), NumAttyDict(a=2), NumAttyDict(a=19, b=45)),
    ],
)
def test_oop_floor_division_with_other(x, y, expected):
    orig_x = deepcopy(x)
    orig_y = deepcopy(y)

    assert x // y == expected
    assert x == orig_x
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3, extra=4), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2), NumDict(a=1.54, b=0.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2), NumAttyDict(a=1.54, b=0.5)),
    ],
)
def test_oop_modulus_with_other(x, y, expected):
    orig_x = deepcopy(x)
    orig_y = deepcopy(y)

    assert x % y == expected
    assert x == orig_x
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumDict(a=5.54, b=7.5)),
        (NumDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumDict(a=5.54, b=7.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3, extra=4), NumDict(a=5.54, b=7.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2), NumDict(a=5.54, b=4.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumAttyDict(a=5.54, b=7.5)),
        (NumAttyDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumAttyDict(a=5.54, b=7.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=5.54, b=7.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2), NumAttyDict(a=5.54, b=4.5)),
    ],
)
def test_inplace_addition_with_other(x, y, expected):
    orig_y = deepcopy(y)

    x += y
    assert x == expected
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3, extra=4), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2), NumDict(a=1.54, b=4.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2), NumAttyDict(a=1.54, b=4.5)),
    ],
)
def test_inplace_subtraction_with_other(x, y, expected):
    orig_y = deepcopy(y)

    x -= y
    assert x == expected
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumDict(a=7.08, b=13.5)),
        (NumDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumDict(a=7.08, b=13.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3, extra=4), NumDict(a=7.08, b=13.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2), NumDict(a=7.08, b=4.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumAttyDict(a=7.08, b=13.5)),
        (NumAttyDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumAttyDict(a=7.08, b=13.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=7.08, b=13.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2), NumAttyDict(a=7.08, b=4.5)),
    ],
)
def test_inplace_multiplication_with_other(x, y, expected):
    orig_y = deepcopy(y)

    x *= y
    assert x == expected
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumDict(a=1.77, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumDict(a=1.77, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3, extra=4), NumDict(a=1.77, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2), NumDict(a=1.77, b=4.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumAttyDict(a=1.77, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumAttyDict(a=1.77, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=1.77, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2), NumAttyDict(a=1.77, b=4.5)),
    ],
)
def test_inplace_division_with_other(x, y, expected):
    orig_y = deepcopy(y)

    x /= y
    assert x == expected
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3, b=4), NumDict(a=2, b=3), NumDict(a=9, b=64)),
        (NumDict(a=3, b=4), NumAttyDict(a=2, b=3), NumDict(a=9, b=64)),
        (NumDict(a=3, b=4), NumDict(a=2, b=3, extra=4), NumDict(a=9, b=64)),
        (NumDict(a=3, b=4), NumDict(a=2), NumDict(a=9, b=4)),
        (NumAttyDict(a=3, b=4), NumAttyDict(a=2, b=3), NumAttyDict(a=9, b=64)),
        (NumAttyDict(a=3, b=4), NumDict(a=2, b=3), NumAttyDict(a=9, b=64)),
        (NumAttyDict(a=3, b=4), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=9, b=64)),
        (NumAttyDict(a=3, b=4), NumAttyDict(a=2), NumAttyDict(a=9, b=4)),
    ],
)
def test_inplace_power_with_other(x, y, expected):
    orig_y = deepcopy(y)

    x **= y
    assert x == expected
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=39, b=45), NumDict(a=2, b=3), NumDict(a=19, b=15)),
        (NumDict(a=39, b=45), NumAttyDict(a=2, b=3), NumDict(a=19, b=15)),
        (NumDict(a=39, b=45), NumDict(a=2, b=3, extra=4), NumDict(a=19, b=15)),
        (NumDict(a=39, b=45), NumDict(a=2), NumDict(a=19, b=45)),
        (NumAttyDict(a=39, b=45), NumAttyDict(a=2, b=3), NumAttyDict(a=19, b=15)),
        (NumAttyDict(a=39, b=45), NumDict(a=2, b=3), NumAttyDict(a=19, b=15)),
        (NumAttyDict(a=39, b=45), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=19, b=15)),
        (NumAttyDict(a=39, b=45), NumAttyDict(a=2), NumAttyDict(a=19, b=45)),
    ],
)
def test_inplace_floor_division_with_other(x, y, expected):
    orig_y = deepcopy(y)

    x //= y
    assert x == expected
    assert y == orig_y


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2, b=3, extra=4), NumDict(a=1.54, b=1.5)),
        (NumDict(a=3.54, b=4.5), NumDict(a=2), NumDict(a=1.54, b=0.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumDict(a=2, b=3), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2, b=3, extra=4), NumAttyDict(a=1.54, b=1.5)),
        (NumAttyDict(a=3.54, b=4.5), NumAttyDict(a=2), NumAttyDict(a=1.54, b=0.5)),
    ],
)
def test_inplace_modulus_with_other(x, y, expected):
    orig_y = deepcopy(y)

    x %= y
    assert x == expected
    assert y == orig_y


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), NumAttyDict(a=1.54, b=2.1)])
def test_scalar_ge(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v >= 2 for k, v in x.items()})
    y = x >= 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3, b=4), NumDict(a=2, b=6), NumDict(a=True, b=False)),
        (NumDict(a=3, b=4), NumAttyDict(a=2, b=6), NumDict(a=True, b=False)),
        (NumAttyDict(a=3, b=4), NumAttyDict(a=2, b=6), NumAttyDict(a=True, b=False)),
        (NumAttyDict(a=3, b=4), NumDict(a=2, b=6), NumAttyDict(a=True, b=False)),
    ],
)
def test_oop_ge_with_other(x, y, expected):
    orig_x = deepcopy(x)
    orig_y = deepcopy(y)

    assert (x >= y) == expected
    assert x == orig_x
    assert y == orig_y


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), NumAttyDict(a=1.54, b=2.1)])
def test_scalar_gt(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v > 2 for k, v in x.items()})
    y = x > 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3, b=4), NumDict(a=2, b=6), NumDict(a=True, b=False)),
        (NumDict(a=3, b=4), NumAttyDict(a=2, b=6), NumDict(a=True, b=False)),
        (NumAttyDict(a=3, b=4), NumAttyDict(a=2, b=6), NumAttyDict(a=True, b=False)),
        (NumAttyDict(a=3, b=4), NumDict(a=2, b=6), NumAttyDict(a=True, b=False)),
    ],
)
def test_oop_gt_with_other(x, y, expected):
    orig_x = deepcopy(x)
    orig_y = deepcopy(y)

    assert (x > y) == expected
    assert x == orig_x
    assert y == orig_y


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), NumAttyDict(a=1.54, b=2.1)])
def test_scalar_lt(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v < 2 for k, v in x.items()})
    y = x < 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3, b=4), NumDict(a=2, b=6), NumDict(a=False, b=True)),
        (NumDict(a=3, b=4), NumAttyDict(a=2, b=6), NumDict(a=False, b=True)),
        (NumAttyDict(a=3, b=4), NumAttyDict(a=2, b=6), NumAttyDict(a=False, b=True)),
        (NumAttyDict(a=3, b=4), NumDict(a=2, b=6), NumAttyDict(a=False, b=True)),
    ],
)
def test_oop_lt_with_other(x, y, expected):
    orig_x = deepcopy(x)
    orig_y = deepcopy(y)

    assert (x < y) == expected
    assert x == orig_x
    assert y == orig_y


@pytest.mark.parametrize('x,', [NumDict(a=1.54, b=2.1), NumAttyDict(a=1.54, b=2.1)])
def test_scalar_le(x):
    orig = deepcopy(x)
    expected = x.__class__({k: v <= 2 for k, v in x.items()})
    y = x <= 2
    assert y == expected
    assert isinstance(y, x.__class__)
    assert x == orig


@pytest.mark.parametrize(
    'x, y, expected',
    [
        (NumDict(a=3, b=4), NumDict(a=2, b=6), NumDict(a=False, b=True)),
        (NumDict(a=3, b=4), NumAttyDict(a=2, b=6), NumDict(a=False, b=True)),
        (NumAttyDict(a=3, b=4), NumDict(a=2, b=6), NumAttyDict(a=False, b=True)),
        (NumAttyDict(a=3, b=4), NumAttyDict(a=2, b=6), NumAttyDict(a=False, b=True)),
    ],
)
def test_oop_le_with_other(x, y, expected):
    orig_x = deepcopy(x)
    orig_y = deepcopy(y)

    assert (x <= y) == expected
    assert x == orig_x
    assert y == orig_y


def test_invalid_comparison_with_non_matching_keys():
    msg = 'cannot compare NumDict to NumDict when keys do not match!'
    with pytest.raises(RuntimeError, match=msg):
        NumDict(a=1) >= NumDict(a=1, b=5)  # noqa: B015


def test_round():
    nd = NumDict(a=3.56, b=3.1)
    assert round(nd) == NumDict({'a': 4, 'b': 3})
    assert round(nd, 1) == NumDict({'a': 3.6, 'b': 3.1})


def test_abs():
    nd = NumDict(a=-3.56, b=3.1)
    assert abs(nd) == NumDict(a=3.56, b=3.1)


def test_neg():
    nd = NumDict(a=-3.56, b=3.1)
    assert -nd == NumDict(a=3.56, b=-3.1)


def test_mean():
    nd = NumDict(a=-3.56, b=3.1, c=6.4, d=2)
    assert nd.mean() == 1.985


def test_sum():
    nd = NumDict(a=-3.56, b=3.1, c=6.4, d=2)
    assert nd.sum() == 7.94


def test_min():
    nd = NumDict(a=-3.56, b=3.1, c=6.4, d=2)
    assert nd.min() == -3.56


def test_max():
    nd = NumDict(a=-3.56, b=3.1, c=6.4, d=2)
    assert nd.max() == 6.4


def test_equality_with_scalar():
    nd = NumDict(a=-3.56, b=3.1, c=6.4, d=6.4)
    assert (nd == 6.4) == NumDict(a=False, b=False, c=True, d=True)


def test_missing_key_raises_attribute_error_if_accessed_from_attr():
    nd = NumAttyDict(a=1, b=2)
    assert nd.a == 1
    with pytest.raises(AttributeError):
        nd.c
