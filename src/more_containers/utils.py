from typing import Any, Mapping

import keyword


def is_valid_identifier(s: str) -> bool:
    """determines if a str is valid python identifier.
    """
    return s.isidentifier() and not keyword.iskeyword(s)


def is_mapping(obj: Any) -> bool:
    return isinstance(obj, Mapping)
