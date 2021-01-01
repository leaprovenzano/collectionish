from typing import Dict
from numbers import Number
from collectionish.mixins import NumericMixin, DictAttrAccessMixin


class NumDict(Dict[str, Number], NumericMixin):
    """A dictionary that you can do basic math with as though it was a number."""

    def _is_supported_value(self, value) -> bool:
        return isinstance(value, Number)

    def _is_supported_object(self, other) -> bool:
        return isinstance(other, NumDict)

    def _set(self, k, v):
        self[k] = v

    def _get(self, k, default=None):
        if default is not None:
            return self[k]
        return self.get(k, default)

    def _items(self):
        return self.items()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({dict.__repr__(self)})'


class AttyNumDict(NumDict, DictAttrAccessMixin):
    pass
