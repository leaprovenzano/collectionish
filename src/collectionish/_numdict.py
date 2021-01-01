from typing import Dict, Union, Any, Optional
from numbers import Number
import operator

NumT = Union[int, float, Number]


class NumDict(Dict[str, NumT]):
    """A dictionary that you can do basic math with as though it was a number.

    **Supported Operations**:
        - addition (+)
        - subtraction (-)
        - multiplication (*)
        - division (/)
        - floor division (//)
        - power (**)
        - modulus (%)
        - ge (>=) -- for scalars or numdicts with matching keys
        - gt (>) -- for scalars or numdicts with matching keys
        - lt (<=) -- for scalars or numdicts with matching keys
        - le (<) -- for scalars or numdicts with matching keys
        - negation (-)
        - abs
        - round

    Example:
        >>> from collectionish import NumDict
        >>>
        >>> nd = NumDict(a =-3.56, b=6.4)
        >>> nd
        NumDict({'a': -3.56, 'b': 6.4})

        numdicts support arithmetic via builtin operators on scalar with scalar values:

        >>> nd + 1
        NumDict({'a': -2.56, 'b': 7.4})

        >>> 1 + nd
        NumDict({'a': -2.56, 'b': 7.4})

        including inplace ops:

        >>> nd += 1
        >>> nd
        NumDict({'a': -2.56, 'b': 7.4})

        likewise with other numdicts

        >>> nd * NumDict(a=2, b=4)
        NumDict({'a': -5.12, 'b': 29.6})

        >>> nd *= NumDict(a=2, b=4)
        >>> nd
        NumDict({'a': -5.12, 'b': 29.6})

        when doing math on numdicts that dont share all keys
        we try and stay do the sensible thing....

        keys are taken from the lefthand numberdict and will be ordered as such.
        so any extra keys in the rightand numberdict will be ignored.

        >>> x = NumDict(a =-3.56, b=6.4)
        >>> y = NumDict(a =2, b=4, extra=6)
        >>> x * y
        NumDict({'a': -7.12, 'b': 25.6})

        if a key is missing from the righthand numberdict we treat the missing bit
        as the identity value for that operation:

        0 for addition, subtraction &
         1 for multiplication, division, exponentiation, floor division and modulus


        >>> x = NumDict(a =-3.56, b=6.4)
        >>> y = NumDict(a =2, extra=6) # no b!
        >>> x * y
        NumDict({'a': -7.12, 'b': 6.4})

        numdicts support basic builtins like round and abs:

        >>> nd = NumDict(a = -3.56, b=3.1, c=6.4, d=2)
        >>> round(nd)
        NumDict({'a': -4, 'b': 3, 'c': 6, 'd': 2})

        >>> round(nd, 1)
        NumDict({'a': -3.6, 'b': 3.1, 'c': 6.4, 'd': 2})

        >>> abs(nd)
        NumDict({'a': 3.56, 'b': 3.1, 'c': 6.4, 'd': 2})


        as well as a couple extra aggregation methods:

        >>> nd.sum()
        7.94

        >>> nd.min()
        -3.56

        >>> nd.max()
        6.4

        >>> nd.mean()
        1.985
    """

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
        """return the minimum value in this numdict."""
        return min(self.values())

    def max(self):
        """return the maximum value in this numdict."""
        return max(self.values())

    def sum(self):
        """return the sum of the values in this numdict."""
        return sum(self.values())

    def mean(self):
        """return the mean (average) of the values in this numdict."""
        return self.sum() / len(self)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({dict.__repr__(self)})'


class NumAttyDict(NumDict):
    """A numeric dict like :class:`NumDict` with attribute access to keys.

    supports all the same operations as regular :class:`NumDict`.

    Example:
        >>> from collectionish import NumAttyDict
        >>>
        >>> nd = NumAttyDict(a =-3.56, b=6.4)
        >>> nd += 2
        >>> nd.a
        -1.56

        >>> nd.b
        8.4


    """

    def __getattr__(self, key: str):
        try:
            return self[key]  # type:ignore
        except KeyError:
            raise AttributeError(key)
