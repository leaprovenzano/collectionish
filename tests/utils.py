import pytest


def mark_params(f):
    return pytest.mark.parametrize(f._argnames, f._params)(f)


def param(tag=None, **kwargs):
    def wrapper(f):
        seen = hasattr(f, '_argnames') and hasattr(f, '_params')
        if not seen:
            f._argnames = tuple(kwargs)
            f._params = []
        p = pytest.param(*[kwargs[k] for k in f._argnames], id=tag)
        f._params.append(p)
        return f

    return wrapper
