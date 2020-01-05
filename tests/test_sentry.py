import pytest
import pickle

from collectionish._sentry import Sentry

SENTRY = Sentry()


def test_sentry_may_not_be_subclassed():
    with pytest.raises(TypeError):

        class SubSentry(Sentry):

            pass


def test_setattr_on_sentry_fails(sentry: Sentry = SENTRY):
    with pytest.raises(AttributeError):
        sentry.apples = 1


def test_sentry_evaluates_false(sentry: Sentry = SENTRY):
    if sentry:
        pytest.fail('Sentry objects should eval False')


def test_pickle_sentry(subtests):
    unpickled = pickle.loads(pickle.dumps(SENTRY))

    with subtests.test(msg='test equality on unpickled sentry'):
        assert SENTRY == unpickled

    with subtests.test(msg='test_sentry_evaluates_false(unpickled)'):
        test_sentry_evaluates_false(unpickled)

    with subtests.test(msg='test_setattr_on_sentry_fails(unpickled)', i=3):
        test_setattr_on_sentry_fails(unpickled)
