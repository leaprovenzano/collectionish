# collectionish

Collectionish is a pure python library extending the basic collection data types and operations for working with them.

----
[![pypi version](https://img.shields.io/pypi/v/collectionish.svg)](https://pypi.python.org/pypi/collectionish)
[![build](https://github.com/leaprovenzano/collectionish/workflows/CI/badge.svg)](https://github.com/leaprovenzano/collectionish/actions)
[![documentation status](https://readthedocs.org/projects/collectionish/badge/?version=latest)](https://collectionish.readthedocs.io/en/latest/?badge=latest)
[![coverage](https://codecov.io/gh/leaprovenzano/collectionish/branch/master/graph/badge.svg)](https://codecov.io/gh/leaprovenzano/collectionish/branch/master/graph/badge.svg)
------------------------------------------------------------------------

-   *Free software*: MIT license
-   *Documentation*: [docs](https://collectionish.readthedocs.io)
-   *Supported Python Versions*: >=3.7

------------------------------------------------------------------------

## Getting Started:


Install the latest stable version with pip:

    $ pip install collectionish

---
## Checkout the docs:

It's best to checkout the [docs](https://collectionish.readthedocs.io). There you'll find detailed
documentation of collectionish's features and lots of examples of how to
use them.

--

## What's is it?

Python is a wonderful language when it comes to extending inbuilt types
and making things that quack. `collectionish` subscribes to the ideology
that the behaviour of data structures belongs *in* data structures and
that it's better and more graceful to bake the behavior into a type than
to complicate surrounding business logic creating many more wtf moments
and room for bugs to sneak in.

Python's own [collections][https://docs.python.org/library/collections.html] module is a great example. take
`defaultdict`, how many times have you seen something like this?

``` python
pets = [('cat', 'tabby'),
        ('cat', 'ginger'),
        ('dog', 'beagle'),
        ('dog', 'poodle'),
        ('lizard', 'gecko')
       ]

pet_dict = {}
for typ, subtyp in pets:
    try:
        pet_dict[typ].append(subtyp)
    except KeyError:
        # now we'll need to make an comment to explain...
        # if the key doesn't exist pet_dict we make a new
        # list containing the pet's subtype
        pet_dict[typ] = [subtyp]
```

vs:

``` python
from collections import defaultdict

pet_dict = defaultdict(list)
for typ, subtyp in pets:
    pet_dict[typ].append(subtyp)
```

`collectionish` adds some extra collections such like ``AttyDict`` (a
straightforward recursive dot access `dict` ) and ``UniqueTuple`` ( a
tuple of unique items that remembers insertion order). New collections
will be added fairly regularly on the basis that they are generic enough
and useful enough that i find myself repeating them in other projects.

In addition to data structures `collectionish` also provides some
operations for working with data structures (from both standard python
and `collections`) like the recursive getters and setters
``collectionish.ops``.

---

## Principles:

**useful enough:**  
Inspirations for data structures should come from stuff we've written or
needed before at some point.

**generic enough:**  
To be extended within reason.

**specific enough:**  
To be clear about what things do. We don't aim to make *the* data
structure or stand in for a pandas dataframe that does everything.

**intuitive enough**:  
type hinting should generally work the same as it does with parent
types, signatures should not be wildly different, obvious magic methods
or such as `__iter__` should not generally be missing from data types.

**documented enough:**  
All public structures and ops should be documented and have doctest
examples so we know its correct and It should be fairly obvious from
somethings name what it is.

**tested more than enough:**  
we test with the excellent [hypothesis][https://github.com/HypothesisWorks/hypothesis] library
wherever possible. We do doctests to keep documentation correct.
