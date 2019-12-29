from typing import Any, Iterable
from functools import reduce


def rgetattr(obj: Any, *keys: Iterable[str]):
    """A recursive version of :function:`python:getattr`.

    Example:

        Here's a simple example using :class:`python:types.SimpleNamespace` as a standin for \
        anything with attibute access:

        >>> from types import SimpleNamespace
        >>> from more_containers.ops import rgetattr
        >>>
        >>> thing = SimpleNamespace(a=1, b=SimpleNamespace(ba=1, bb=SimpleNamespace(bba=1, bbb=2)))

        with only one key it works like normal :function:`python:getattr`:

        >>> rgetattr(thing, 'a')
        1
        >>> rgetattr(thing, 'b')
        namespace(ba=1, bb=namespace(bba=1, bbb=2))

        with multiple ``rgetattr`` gathers the attibute from a nested object:

        >>> rgetattr(thing, 'b', 'ba')
        1
        >>> rgetattr(thing, 'b', 'bb', 'bbb')
        2

    """
    return reduce(getattr, keys, obj)  # type: ignore
