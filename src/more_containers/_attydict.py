from typing import Dict, TypeVar

from more_containers.utils import is_valid_identifier

T = TypeVar('T')


class attydict(Dict[str, T]):  # noqa : N801

    """a classic dict with dot access.

    Example:

        initilize a basic attydict
        >>> from more_containers import attydict
        >>>
        >>> the_sea = attydict(crabs=10, fish=2)
        >>> the_sea
        {'crabs': 10, 'fish': 2}

        access stuff with dots
        >>> the_sea.crabs += 1
        >>> the_sea.crabs
        11

        nested stuff will also have attr access
        >>> the_sea.update(submarines= {'sandwich': 0, 'actual': 1})
        >>> the_sea
        {'crabs': 11, 'fish': 2, 'submarines': {'sandwich': 0, 'actual': 1}}
        >>> the_sea.submarines.actual
        1

        we handle name clashes in a similar way to pandas -
        Reserved names can be set using standard dict access:
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
                return type(value)((cls._attrify(v) for v in value))
            if isinstance(value, dict) and not isinstance(value, cls):
                return cls(**value)
        return value

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setitem__(k, v)

    def _validate_key(self, s: str):
        if not isinstance(s, str):
            raise TypeError(f'{self.__class__.__name__} keys must be strings.')
        if not is_valid_identifier(s):
            raise SyntaxError(f'{self.__class__.__name__} keys must be valid python identifiers.')

    def __getattr__(self, key: str) -> T:
        return self[key]

    def __setattr__(self, key: str, value: T):
        self[key] = value

    def __setitem__(self, key: str, value: T):
        if key not in self:
            self._validate_key(key)
        dict.__setitem__(self, key, self._attrify(value))

    def update(self, **kwargs):
        for k, v in kwargs.items():
            self[k] = v


# alias as lower
AttyDict = attydict
