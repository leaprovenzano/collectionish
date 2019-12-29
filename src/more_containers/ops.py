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


def rsetattr(obj: Any, keys: Iterable[str], value: Any):
    """A recursive version of :function:`python:setattr`.

    Example:

        Again we'll use :class:`python:types.SimpleNamespace` as a standin for \
        anything with attibute access:

        >>> from types import SimpleNamespace
        >>> from more_containers.ops import rgetattr
        >>>
        >>> thing = SimpleNamespace()

        with only one key it works like normal :function:`python:setattr`:

        >>> rsetattr(thing, ['a'], 1)
        >>> thing
        namespace(a=1)
        >>> rsetattr(thing, ['b'], SimpleNamespace(ba= 1, bb= 2))
        >>> thing
        namespace(a=1, b=namespace(ba=1, bb=2))

        with multiple ``rsetattr`` can update a nested value:

        >>> rsetattr(thing, ('b', 'ba'), 2)
        >>> thing
        namespace(a=1, b=namespace(ba=2, bb=2))

    """
    *keys, last = keys
    parent = rgetattr(obj, *keys)
    setattr(parent, last, value)
