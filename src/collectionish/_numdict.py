from typing import Dict, Any, Callable, TypeVar
from numbers import Number
import operator

T = TypeVar('T')


def _unpack_args(iterable_or_mapping=None, **kwargs):
    if iterable_or_mapping:
        if isinstance(iterable_or_mapping, dict):
            yield from iterable_or_mapping.items()
        else:
            yield from iterable_or_mapping
    yield from kwargs.items()


class NumDict(Dict[str, T]):
    """A dictionary that you can do basic math with as though it was a number."""

    def __init__(self, iterable_or_mapping=None, **kwargs):
        for k, v in _unpack_args(iterable_or_mapping, **kwargs):
            self.__setitem__(k, v)

    def _apply_op_with_mapping(self, op, mapping, noop) -> 'NumDict':
        return self.__class__({k: op(v, mapping.get(k, noop)) for k, v in self.items()})

    def _apply_op_with_value(self, op, value) -> 'NumDict':
        return self.__class__({k: op(v, value) for k, v in self.items()})

    def _rapply_op_with_value(self, op, value) -> 'NumDict':
        return self.__class__({k: op(value, v) for k, v in self.items()})

    def _iapply_op_with_value(self, op, value) -> 'NumDict':
        for k in self:
            self[k] = op(self[k], value)
        return self

    def _iapply_op_with_mapping(self, op, mapping, noop) -> 'NumDict':
        for k in self:
            self[k] = op(self[k], mapping.get(k, noop))
        return self

    def _is_supported_value(self, value) -> bool:
        return isinstance(value, Number)

    def _is_supported_mapping(self, other) -> bool:
        return isinstance(other, NumDict)

    def _apply_with_other(self, op, other: Any, noop=None):
        if self._is_supported_mapping(other):
            return self._apply_op_with_mapping(op, other, noop=noop)
        elif self._is_supported_value(other):
            return self._apply_op_with_value(op, other)
        return NotImplemented

    def _iapply_with_other(self, op, other: Any, noop=None):
        if self._is_supported_mapping(other):
            return self._iapply_op_with_mapping(op, other, noop=noop)
        elif self._is_supported_value(other):
            return self._iapply_op_with_value(op, other)
        return NotImplemented

    def _rapply_with_other(self, op, other: Any):
        if self._is_supported_value(other):
            return self._rapply_op_with_value(op, other)
        return NotImplemented

    # standard numeric modifiers

    def __abs__(self):
        return self.__class__({k: abs(v) for k, v in self.items()})

    def __round__(self, places: int = 1):
        return self.__class__({k: round(v, places) for k, v in self.items()})

    def __neg__(self):
        return self.__class__({k: -v for k, v in self.items()})

    def __pos__(self):
        return self.__class__({k: +v for k, v in self.items()})

    def __inv__(self):
        return self.__class__({k: ~v for k, v in self.items()})

    # comparison ops

    def __eq__(self, other: Any):
        return self._apply_with_other(operator.eq, other, noop=False)

    def __ne__(self, other: Any):
        return self._apply_with_other(operator.ne, other, noop=False)

    def __ge__(self, other: Any):
        return self._apply_with_other(operator.ge, other, noop=False)

    def __le__(self, other: Any):
        return self._apply_with_other(operator.le, other, noop=False)

    def __gt__(self, other: Any):
        return self._apply_with_other(operator.gt, other, noop=False)

    def __lt__(self, other: Any):
        return self._apply_with_other(operator.lt, other, noop=False)

    def __or__(self, other: Any):
        return self._apply_with_other(operator.or_, other, noop=False)

    def __ior__(self, other: Any):
        return self._iapply_with_other(operator.or_, other, noop=False)

    def __xor__(self, other: Any):
        return self._apply_with_other(operator.xor, other, noop=False)

    def __ixor__(self, other: Any):
        return self._iapply_with_other(operator.ixor, other, noop=False)

    def __and__(self, other: Any):
        return self._apply_with_other(operator.and_, other, noop=False)

    def __iand__(self, other: Any):
        return self._iapply_with_other(operator.and_, other, noop=False)

    # arithmetic ops

    def __add__(self, other: Any):
        return self._apply_with_other(operator.add, other, noop=0)

    def __iadd__(self, other: Any):
        return self._iapply_with_other(operator.add, other)

    def __radd__(self, other: Any):
        return self._rapply_with_other(operator.add, other)

    def __sub__(self, other: Any):
        return self._apply_with_other(operator.sub, other, noop=0)

    def __isub__(self, other: Any):
        return self._iapply_with_other(operator.sub, other, noop=0)

    def __rsub__(self, other: Any):
        return self._rapply_with_other(operator.sub, other)

    def __mul__(self, other: Any):
        return self._apply_with_other(operator.mul, other, noop=1)

    def __imul__(self, other: Any):
        return self._iapply_with_other(operator.mul, other, noop=1)

    def __rmul__(self, other: Any):
        return self._rapply_with_other(operator.mul, other)

    def __truediv__(self, other: Any):
        return self._apply_with_other(operator.truediv, other, noop=1)

    def __itruediv__(self, other: Any):
        return self._iapply_with_other(operator.truediv, other, noop=1)

    def __rtruediv__(self, other: Any):
        return self._rapply_with_other(operator.pow, other)

    def __pow__(self, other: Any):
        return self._apply_with_other(operator.pow, other, noop=1)

    def __ipow__(self, other: Any):
        return self._iapply_with_other(operator.pow, other, noop=1)

    def __rpow__(self, other: Any):
        return self._rapply_with_other(operator.pow, other)

    def __mod__(self, other: Any):
        return self._apply_with_other(operator.mod, other, noop=1)

    def __imod__(self, other: Any):
        return self._iapply_with_other(operator.mod, other, noop=1)

    def __rmod__(self, other: Any):
        return self._rapply_with_other(operator.mod, other)

    def __floordiv__(self, other: Any):
        return self._apply_with_other(operator.floordiv, other, noop=1)

    def __ifloordiv__(self, other: Any):
        return self._iapply_with_other(operator.floordiv, other, noop=1)

    def __rfloordiv__(self, other: Any):
        return self._rapply_with_other(operator.floordiv, other)

    # special aggregation ops

    def min(self):
        return min(self.values())

    def max(self):
        return max(self.values)

    def sum(self):
        return sum(self.values())

    def mean(self):
        return self.sum() / len(self)

    # user facing apply func
    def apply(self, op: Callable[[Number], Number], *args, **kwargs) -> 'NumDict':
        return self.__class__({k: op(v, *args, **kwargs) for k, v in self.items()})
