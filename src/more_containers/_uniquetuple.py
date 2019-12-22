from typing import Tuple, TypeVar, Hashable, Sequence


T = TypeVar('T', bound=Hashable, covariant=True)


class uniquetuple(Tuple[T, ...]):  # noqa : N801

    """An immutable sequence of unique and hashable items ordered by first appearance.

    - like ``tuple`` and ``frozenset``,  ``uniquetuple`` is immutable.
    - like ``frozenset``, ``uniquetuple`` accepts only hashable values.
    - `unlike` ``frozenset``, ``uniquetuple`` cares about insertion order. \
    It orders by will be ordered by first appearance.
    - finally ``uniquetuple`` may be initilized with an unpacked iterable.

    Example:

        >>> from more_containers import uniquetuple
        >>>
        >>> uniquetuple(3, 2, 3, 1)
        uniquetuple(3, 2, 1)

    """

    def __new__(cls, *args: Sequence[T]):
        # since dict remembers insertion order we can just use that with no values
        return super().__new__(cls, dict({arg: None for arg in args}))  # type: ignore

    def count(self, value) -> int:
        return int(value in self)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{super().__repr__()}'


# alias as lower like tuple
UniqueTuple = uniquetuple
