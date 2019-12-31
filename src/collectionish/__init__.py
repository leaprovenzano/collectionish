# -*- coding: utf-8 -*-

"""collectionish is a repository of possibly useful, fairly generic container types.
"""

__author__ = """Lea Provenzano"""
__email__ = 'leaprovenzano@gmail.com'
__version__ = '0.1.2'

# this is exists to make sphinx happy
__all__ = ['UniqueTuple', 'AttyDict']


from ._uniquetuple import UniqueTuple
from ._attydict import AttyDict
