from typing import Any, Optional, Callable, TypeVar, SupportsIndex
from numbers import Number
import operator

T = TypeVar('T')


class NumericMixin:
    def _is_supported_value(self, value) -> bool:
        return isinstance(value, Number)

    def _is_supported_object(self, other) -> bool:
        return isinstance(other, self.__class__)

    def _set(self, k, v):
        setattr(self, k, v)

    def _get(self, k, default=None):
        return getattr(self, k, default)

    def _items(self):
        return self.__dict__.items()

    def _apply_op_with_obj(self, op, obj, noop):
        return self.__class__(**{k: op(self._get(k, noop)) for k, v in self._items()})

    def _apply_op_with_value(self, op, value):
        return self.__class__(**{k: op(v, value) for k, v in self._items()})

    def _rapply_op_with_value(self, op, value):
        return self.__class__(**{k: op(value, v) for k, v in self._items()})

    def _iapply_op_with_value(self, op, value):
        for k in self:
            self._set(k, op(self._get(k), value))
        return self

    def _iapply_op_with_obj(self, op, obj, noop):
        for k in self:
            self._set(k, op(self._get(k), obj._get(k, noop)))
        return self

    def _apply_with_other(self, op, other: Any, noop=None):
        if self._is_supported_object(other):
            return self._apply_op_with_obj(op, other, noop=noop)
        elif self._is_supported_value(other):
            return self._apply_op_with_value(op, other)
        return NotImplemented

    def _iapply_with_other(self, op, other: Any, noop=None):
        if self._is_supported_object(other):
            return self._iapply_op_with_obj(op, other, noop=noop)
        elif self._is_supported_value(other):
            return self._iapply_op_with_value(op, other)
        return NotImplemented

    def _rapply_with_other(self, op, other: Any):
        if self._is_supported_value(other):
            return self._rapply_op_with_value(op, other)
        return NotImplemented

    # standard numeric modifiers

    def __abs__(self):
        return self.__class__(**{k: abs(v) for k, v in self._items()})  # type: ignore

    def __round__(self, places: Optional[int] = None):
        return self.__class__(**{k: round(v, places) for k, v in self._items()})  # type: ignore

    def __neg__(self):
        return self.__class__(**{k: -v for k, v in self._items()})  # type: ignore

    def __pos__(self):
        return self.__class__(**{k: +v for k, v in self._items()})  # type: ignore

    def __inv__(self):
        return self.__class__(**{k: ~v for k, v in self._items()})  # type: ignore

    # comparison ops

    def __eq__(self, other: Any):
        if self._is_supported_value(other):
            return self._apply_op_with_value(operator.eq, other)
        else:
            return super().__eq__(other)

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
    def apply(self, op: Callable[[Number], Number], *args, **kwargs):
        return self.__class__(
            **{k: op(v, *args, **kwargs) for k, v in self._items()}  # type:ignore
        )


class DictAttrAccessMixin(SupportsIndex):
    def __getattr__(self, key: str) -> T:
        return self[key]  # type:ignore
