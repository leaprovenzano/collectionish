from typing import Dict, TypeVar, Iterable, Mapping, Optional, Tuple, Union

from collectionish.utils import is_valid_identifier

T = TypeVar('T')
InitFromT = Union[Mapping[str, T], Iterable[Tuple[str, T]]]


def _unpack_args(iterable_or_mapping: Optional[InitFromT] = None, **kwargs):
    if iterable_or_mapping:
        if isinstance(iterable_or_mapping, dict):
            yield from iterable_or_mapping.items()
        else:
            yield from iterable_or_mapping
    yield from kwargs.items()


class AttyDict(Dict[str, T]):

    """A lightweight dictionary with dot access.

    ``attydicts`` are dictionaries witch allow access to values values through dot notation.
    The limitation there is that their keys must be strings ( and valid python identifiers )
    but sometimes this is what you want when working with json objects unpredictable json
    or the like. That said, if you have sturctured data you'd  of course be much better off \
    using a structured datatype.

    Example:

        initilize a basic attydict:

        >>> from collectionish import AttyDict
        >>>
        >>> the_sea = AttyDict(crabs=10, fish=2)
        >>> the_sea
        {'crabs': 10, 'fish': 2}

        access stuff with dots:

        >>> the_sea.crabs += 1
        >>> the_sea.crabs
        11

        nested stuff will also have attr access:

        >>> the_sea.update(submarines= {'sandwich': 0, 'actual': 1})
        >>> the_sea
        {'crabs': 11, 'fish': 2, 'submarines': {'sandwich': 0, 'actual': 1}}
        >>> the_sea.submarines.actual
        1

        we handle name clashes in a similar way to pandas - Reserved names can be set using
        standard dict access:

        >>> the_sea['pop'] = 'corn'
        >>> the_sea
        {'crabs': 11, 'fish': 2, 'submarines': {'sandwich': 0, 'actual': 1}, 'pop': 'corn'}
        >>> the_sea.pop('pop')
        'corn'
        >>> the_sea
        {'crabs': 11, 'fish': 2, 'submarines': {'sandwich': 0, 'actual': 1}}

        and as youd expect lists containing dictionaries just work...

        >>> the_sea.whales = [{'killer': 1}, {'humpback': 2}, 'mr. whale']
        >>> the_sea.whales[1].humpback
        2
    """

    @classmethod
    def _attrify(cls, value):
        if hasattr(value, '__iter__'):
            if isinstance(value, (list, tuple)):
                return type(value)(cls._attrify(v) for v in value)
            if isinstance(value, dict) and not isinstance(value, cls):
                return cls(**value)
        return value

    def __setattr__(self, key: str, value: T):
        self[key] = value

    def __init__(self, iterable_or_mapping: Optional[InitFromT] = None, **kwargs):
        for k, v in _unpack_args(iterable_or_mapping, **kwargs):
            self.__setitem__(k, v)

    def _validate_key(self, s: str):
        if not isinstance(s, str):
            raise TypeError(f'{self.__class__.__name__} keys must be strings.')
        if not is_valid_identifier(s):
            raise SyntaxError(f'{self.__class__.__name__} keys must be valid python identifiers.')

    def __setitem__(self, key: str, value: T):
        if key not in self:
            self._validate_key(key)
        dict.__setitem__(self, key, self._attrify(value))

    def update(self, **kwargs):
        for k, v in kwargs.items():
            self[k] = v

    def __getattr__(self, key: str) -> T:
        try:
            return self[key]  # type:ignore
        except KeyError:
            raise AttributeError(key)
