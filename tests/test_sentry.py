import pytest

from collectionish._sentry import Sentry


def test_sentry_may_not_be_subclassed():
    with pytest.raises(TypeError):

        class SubSentry(Sentry):

            pass


def test_setattr_on_sentry_fails():
    sentry = Sentry()
    with pytest.raises(AttributeError):
        sentry.apples = 1


def test_sentry_evaluates_fase():
    sentry = Sentry()
    if sentry:
        pytest.fail('Sentry objects should eval False')
