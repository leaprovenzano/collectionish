from typing import Any, Iterable, Sequence, Hashable, MutableMapping, Mapping, Union, Tuple
from functools import reduce
from collectionish import AttyDict


def rgetattr(obj: Any, *keys: Iterable[str]):
    """A recursive version of :py:func:`getattr`.

    Example:

        Here's a simple example using :py:class:`types.SimpleNamespace` as a standin for \
        anything with attibute access:

        >>> from types import SimpleNamespace
        >>> from collectionish.ops import rgetattr
        >>>
        >>> thing = SimpleNamespace(a=1, b=SimpleNamespace(ba=1, bb=SimpleNamespace(bba=1, bbb=2)))

        with only one key it works like normal :py:func:`getattr`:

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
    """A recursive version of :py:func:`setattr`.

    Example:

        Again we'll use  :py:class:`types.SimpleNamespace` as a standin for \
        anything with attibute access:

        >>> from types import SimpleNamespace
        >>> from collectionish.ops import rgetattr
        >>>
        >>> thing = SimpleNamespace()

        with only one key it works like normal :py:func:`setattr`:

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


def rgetitem(obj: Union[Sequence, Mapping], *keys: Iterable[Hashable]):
    """A recursive version of :py:func:`__getitem__`.

    Example:

        >>> from collectionish.ops import rgetitem
        >>>
        >>> thing = {'a': 1, 'b': {'ba': 1, 'bb': 2}}

        with only one key it works like normal :py:func:`__getitem__`:

        >>> rgetitem(thing, 'a')
        1

        with multiple ``rgetattr`` gets items recursively:

        >>> rgetitem(thing, 'b', 'bb')
        2

        works fine with lists and stuff as well:

        >>> nested_list = [1, [1, 2, [1, 2, 3]], 2]
        >>> rgetitem(nested_list, -1)
        2
        >>> rgetitem(nested_list, 1, 2, 2)
        3
    """
    return reduce(lambda x, k: x[k], keys, obj)  # type: ignore


def rsetitem(obj: Union[Sequence, MutableMapping], keys: Iterable[Hashable], value: Any) -> None:
    """A recursive version of :py:func:`__setitem__`.

    Example:

        >>> from collectionish.ops import rgetitem
        >>>
        >>> thing = {'a': 1, 'b': {'ba': 1, 'bb': 2}}

        with only one key it works like normal :py:func:`__setitem__`:

        >>> rsetitem(thing, ('a',), 2)
        >>> thing
        {'a': 2, 'b': {'ba': 1, 'bb': 2}}

        with multiple ``rgetattr`` gets items recursively:

        >>> rsetitem(thing, ['b', 'bb'], 4)
        >>> thing
        {'a': 2, 'b': {'ba': 1, 'bb': 4}}

        lists and stuff work as expected:

        >>> nested_list = [1, [1, 2, [1, 2, 3]], 2]
        >>> rsetitem(nested_list, [-1], 3)
        >>> nested_list
        [1, [1, 2, [1, 2, 3]], 3]
        >>> rsetitem(nested_list, [1, 2, 2], 5)
        >>> nested_list
        [1, [1, 2, [1, 2, 5]], 3]

    """
    *keys, last = keys
    parent = rgetitem(obj, *keys)  # type: ignore
    parent[last] = value


def flat_mapping_items(
    mapping: Mapping, delimiter: str = '.', _parent_key: str = ''
) -> Iterable[Tuple[str, Any]]:
    """yield an iterable of compressed keys and values from a possibly nested mapping.

    Args:
        mapping: a possibly nested mapping
        delimiter: string delimiter to use for compressing keys. Defaults to '.'.

    Yields:
        Iterable of compressed key,  value pairs
    """
    for k, v in mapping.items():
        new_key = delimiter.join((_parent_key, k)) if _parent_key else k
        if isinstance(v, Mapping):
            yield from flat_mapping_items(v, delimiter=delimiter, _parent_key=new_key)
        else:
            yield new_key, v


def flatten_mapping(mapping: Mapping, delimiter: str = '.', keep_type: bool = False):
    """flatten a dictionary or other mapping by compressing keys using ``delimiter``.

    Note:
        In the be careful with using ``keep_type`` and a `"."` delimiter with
        an :class:`collectionish.AttyDict`, as attydict keys need to be valid python names
        and therefore should not contain a dot. This function will raise a value
        error and tell you off if you try that.

    Args:
        mapping: a possibly nested mapping
        delimiter: string delimiter to use for compressing keys. Defaults to '.'. Defaults to '.'.
        keep_type: If ``True`` attempt to ensure returned mapping is same
            type as the input mapping otherwise just return a dict. Defaults to False.

    Example:
        >>> from collectionish.ops import flatten_mapping
        >>> nested_dict = {'day': 1,
        ...                'apples': {'eaten': 2, 'left': 4, 'color': {'red':3, 'green': 1}},
        ...                'sausages': {'eaten': 1, 'left': 3, 'gone_off':1}}
        >>>
        >>> print(flatten_mapping(nested_dict, delimiter='.'))
        {'day': 1,
        'apples.eaten': 2,
        'apples.left': 4,
        'apples.color.red': 3,
        'apples.color.green': 1,
        'sausages.eaten': 1,
        'sausages.left': 3,
        'sausages.gone_off': 1}

    """
    if keep_type and delimiter == '.' and isinstance(mapping, AttyDict):
        raise TypeError(
            f'cannot use dot delimiter with {mapping.__class__.__name__}'
            ' try specifying a different delimiter such as an underscore'
            ' or set keep_type to False to return a regular dict.'
        )
    result = dict(flat_mapping_items(mapping, delimiter=delimiter))
    if keep_type:
        return mapping.__class__(result)  # type: ignore
    return result
