from typing import Union, Dict
from collections import ChainMap


class AncestorChainMap(ChainMap):

    """ChainMap variant that allows for the insertion of parents and ancestors.

    Example:
        >>> from collectionish import AncestorChainMap
        >>>
        >>> child = AncestorChainMap({'b': 3, 'c': 3})
        >>> child
        AncestorChainMap({'b': 3, 'c': 3})

        add oldest ancestor:

        >>> child.add_ancestor({'a': 1, 'b': 1})
        >>> child
        AncestorChainMap({'b': 3, 'c': 3}, {'a': 1, 'b': 1})

        add direct parent:

        >>> child.add_parent({'a': 2, 'b': 2})
        >>> child
        AncestorChainMap({'b': 3, 'c': 3}, {'a': 2, 'b': 2}, {'a': 1, 'b': 1})

    """

    def add_parent(self, parent: Union[Dict, ChainMap]):
        """add a parent to the current chain map"""
        self.maps.insert(1, dict(parent))

    def add_ancestor(self, ancestor: Union[Dict, ChainMap]):
        """add a oldest ancestor to the current chain map"""
        return self.maps.append(dict(ancestor))
