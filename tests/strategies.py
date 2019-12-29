from typing import Type, Iterable
from hypothesis import strategies as st


def everything_except(*excluded_types: Iterable[Type]) -> st.SearchStrategy:
    """strategy which returns everything except the excluded types.
    """
    return (
        st.from_type(type).flatmap(st.from_type).filter(lambda x: not isinstance(x, excluded_types))
    )


def one_of_types(*types: Iterable[Type]) -> st.SearchStrategy:
    """return union of type strategies over multiple types.
    """
    return st.one_of(st.from_type(t) for t in types)
