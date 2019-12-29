from typing import Any, Collection, Mapping

import keyword


def is_valid_identifier(s: str) -> bool:
    """determines if a str is valid python identifier.
    """
    return s.isidentifier() and not keyword.iskeyword(s)


def is_mapping(obj: Any) -> bool:
    return isinstance(obj, Mapping)


def is_arraylike(obj: Any) -> bool:
    """Determine if the provided object is an non-mapping generic container type such as an array, tuple or set.

    Example:
        >>> from more_containers.utils import is_arraylike
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
    exclude = (Mapping, str, bytes, bytearray)
    return isinstance(obj, Collection) and not isinstance(obj, exclude)
