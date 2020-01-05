from typing import Any, ClassVar, Optional


class Sentry:

    """A Basic falsey singleton type useful for when ``None`` actually means something.

    Only one instance of Sentry may be created (within a session).
    To prevent weirdness in with import reloads or multiprocessing we test equality /
    based on is tested based on class membership and disallow subclassing.

    The following actions are is forbidden on the Sentry type:
        - subclassing
        - setting attributes
    """

    __slots__ = ()
    _instance: ClassVar[Optional['Sentry']] = None

    def __init_subclass__(cls, *args, **kwargs):
        raise TypeError('Sentry may not be subclassed')

    def __new__(cls) -> 'Sentry':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Sentry)

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}()'
