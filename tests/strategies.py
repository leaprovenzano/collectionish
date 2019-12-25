from hypothesis import strategies as st


def everything_except(*excluded_types) -> st.SearchStrategy:
    """strategy which returns everything except the excluded types.
    """
    return (
        st.from_type(type).flatmap(st.from_type).filter(lambda x: not isinstance(x, excluded_types))
    )
