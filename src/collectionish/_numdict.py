from typing import Dict, Union, Any, Optional
from numbers import Number
import operator

NumT = Union[int, float, Number]


class NumDict(Dict[str, NumT]):
    """A dictionary that you can do basic math with as though it was a number."""

    def _is_supported_value(self, value) -> bool:
        return isinstance(value, Number)

    def _is_supported_object(self, other) -> bool:
        return isinstance(other, NumDict)

    def _apply_op_with_obj(self, op, obj, noop):
        return self.__class__(**{k: op(v, obj.get(k, noop)) for k, v in self.items()})

    def _apply_op_with_value(self, op, value):
        return self.__class__(**{k: op(v, value) for k, v in self.items()})

    def _rapply_op_with_value(self, op, value):
        return self.__class__(**{k: op(value, v) for k, v in self.items()})

    def _iapply_op_with_value(self, op, value):
        for k in self:
            self[k] = op(self[k], value)
        return self

    def _iapply_op_with_obj(self, op, obj, noop):
        for k in self:
            self[k] = op(self[k], obj.get(k, noop))
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

    def _apply_comparison_with_other(self, op, other: Any):
        if self._is_supported_value(other):
            return self._apply_op_with_value(op, other)
        if self._is_supported_object(other):
            if set(self.keys()) == set(other.keys()):
                return self._apply_op_with_obj(op, other, None)
            else:
                raise RuntimeError(
                    f'cannot compare {self.__class__.__name__}'
                    f' to {other.__class__.__name__} when keys do not match!'
                )

        return NotImplemented

    # comparison ops

    def __eq__(self, other: Any):
        if self._is_supported_value(other):
            return self._apply_op_with_value(operator.eq, other)
        else:
            return super().__eq__(other)

    def __ge__(self, other: Any):
        return self._apply_comparison_with_other(operator.ge, other)

    def __le__(self, other: Any):
        return self._apply_comparison_with_other(operator.le, other)

    def __gt__(self, other: Any):
        return self._apply_comparison_with_other(operator.gt, other)

    def __lt__(self, other: Any):
        return self._apply_comparison_with_other(operator.lt, other)

    # standard numeric modifiers

    def __abs__(self):
        return self.__class__(**{k: abs(v) for k, v in self.items()})  # type: ignore

    def __round__(self, places: Optional[int] = None):
        return self.__class__(**{k: round(v, places) for k, v in self.items()})  # type: ignore

    def __neg__(self):
        return self.__class__(**{k: -v for k, v in self.items()})  # type: ignore

    # arithmetic ops

    def __add__(self, other: Any):
        return self._apply_with_other(operator.add, other, noop=0)

    def __iadd__(self, other: Any):
        return self._iapply_with_other(operator.add, other, noop=0)

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
        return self._rapply_with_other(operator.truediv, other)

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

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({dict.__repr__(self)})'


class AttyNumDict(NumDict):
    """A numeric dict like :class:`NumDict` with attribute access to keys."""

    def __getattr__(self, key: str):
        try:
            return self[key]  # type:ignore
        except KeyError:
            raise AttributeError(key)
