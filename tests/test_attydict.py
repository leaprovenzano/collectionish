from typing import Union, Mapping
from copy import deepcopy
import string

from hypothesis import given, assume
from hypothesis import strategies as st
from hypothesis.stateful import (
    RuleBasedStateMachine,
    Bundle,
    rule,
    precondition,
    consumes,
    invariant,
)


from more_containers import attydict
from more_containers.types import AttyDict
from more_containers import ops

from more_containers.utils import is_valid_identifier

from tests.utils import param, mark_params


valid_keys = st.text(string.ascii_lowercase + '_').filter(is_valid_identifier)
flat_values = st.text(string.ascii_lowercase).filter(is_valid_identifier)
nested_values = st.recursive(
    flat_values,
    lambda children: st.one_of(
        st.lists(children, min_size=1),
        st.dictionaries(valid_keys, children, min_size=1),
        st.dictionaries(valid_keys, children, min_size=1).map(lambda x: attydict(**x)),
    ),
    max_leaves=5,
)


def valid_values(*values) -> bool:
    def valid_value(value):
        if isinstance(v, Mapping):
            if not isinstance(v, attydict):
                return False
            return valid_values(value.values())
        elif isinstance(v, (list, tuple, set)):
            return valid_values(*v)
        return True

    for v in values:
        if not valid_value(v):
            return False
    return True


@mark_params
@param(inp=int)
@param(inp=str)
@param(inp=Union[int, str])
def test_typehints(inp):
    hint = AttyDict[inp]
    assert hint.__args__ == (inp,)
    assert hint.__origin__ == AttyDict


@mark_params
@param(tag='flat', inp={'b': 1})
@param(tag='nested', inp={'a': {'aa': 2}})
@param(tag='deep_nested', inp={'a': {'aa': {'aaa': 1}}})
@param(tag='mixed', inp={'a': {'aa': 2}, 'b': 2})
def test_update(inp):
    """Test an attydict update works just the same as a dict update
    """
    atty = attydict(a={'aa': 1, 'ab': 2})
    regular = dict(a={'aa': 1, 'ab': 2})

    atty.update(**inp)
    assert valid_values(atty)

    regular.update(**inp)
    assert dict(atty) == regular


@given(st.dictionaries(valid_keys, nested_values))
def test_init(inp):
    atty = attydict(**inp)
    assert valid_values(atty)
    assert dict(atty) == inp


class AttyDictMachine(RuleBasedStateMachine):

    def __init__(self):
        super().__init__()
        self.atty = attydict()
        self.shadow = dict()
        self.change = 0
        print()

    keys = Bundle('keys')
    values = Bundle('values')

    @rule(target=keys, k=valid_keys)
    def add_new_key(self, k):
        return k

    @precondition(
        lambda self: len([k for k, v in self.atty.items() if isinstance(v, attydict)]) > 0
    )
    @rule(target=keys, existing=st.data(), k=valid_keys)
    def add_nested_key(self, existing, k):
        ex = existing.draw(
            st.sampled_from([k for k, v in self.atty.items() if isinstance(v, attydict)])
        )
        return (ex, k)

    @rule(target=values, v=flat_values)
    def add_flat_value(self, v):
        return v

    @rule(target=values, v=st.dictionaries(keys=valid_keys, values=flat_values))
    def add_dict_values(self, v):
        return v

    @rule(k=consumes(keys), v=consumes(values))
    def set_as_attr(self, k, v):
        print(k, v)
        if isinstance(k, tuple):
            assume(k[0] in self.atty)
            ops.rsetattr(self.atty, k, deepcopy(v))
            ops.rsetitem(self.shadow, k, deepcopy(v))
        else:
            setattr(self.atty, k, deepcopy(v))
            self.shadow[k] = deepcopy(v)
        self.change = 1
        return (k, v)

    @rule(k=consumes(keys), v=consumes(values))
    def set_as_key(self, k, v):
        print(k, v)
        if isinstance(k, tuple):
            assume(k[0] in self.atty)
            ops.rsetitem(self.atty, k, v)
            ops.rsetitem(self.shadow, k, deepcopy(v))
        else:
            self.atty[k] = v
            self.shadow[k] = deepcopy(v)
        self.change = 1
        return (k, v)

    @precondition(lambda self: self.change == 1)
    @invariant()
    def check(self):
        print('-----check-------')
        print('atty:\n', self.atty)
        print('shadow:\n', self.shadow)
        self.change = 0
        assert valid_values(*self.atty.values())
        assert dict(self.atty) == self.shadow
        print('-----------------')


TestAttyDict = AttyDictMachine.TestCase
