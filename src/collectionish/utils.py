from typing import Any, Collection, Mapping

import keyword


def is_valid_identifier(s: str) -> bool:
    """determines if a str is valid python identifier.
    """
    return s.isidentifier() and not keyword.iskeyword(s)


def is_mapping(obj: Any) -> bool:
    """Just a shorthand for instancecheck on :py:class:`typing.Mapping`.
    """
    return isinstance(obj, Mapping)


def is_arraylike(obj: Any) -> bool:
    """Determine if the provided object is an non-mapping generic container type such as an array,\
     tuple or set.

    Example:
        >>> from collectionish.utils import is_arraylike
        >>>
        >>> is_arraylike([1, 2, 3])
        True
        >>> is_arraylike(set([1, 2, 3]))
        True
        >>> is_arraylike(tuple([1, 2, 3]))
        True
        >>> is_arraylike({'a': 1, 'b': 2})
        False
        >>> is_arraylike('a string')
        False
    """
    exclude = (Mapping, str, bytes, bytearray, range, memoryview)
    return isinstance(obj, Collection) and not isinstance(obj, exclude)


def is_hashable(obj: Any) -> bool:
    """Determine if the given object is hashable.

    Example:
        >>> from collectionish.utils import is_hashable
        >>>
        >>> is_hashable([1, 2, 3])
        False
        >>> is_hashable('boop')
        True
    """
    try:
        hash(obj)
        return True
    except TypeError:
        return False
