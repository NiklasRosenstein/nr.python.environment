import sys

from nr.python.environment.distributions import get_distributions, get_distributions_of


def test_get_distributions() -> None:
    assert get_distributions() != {}


def test_get_distributions_of() -> None:
    assert get_distributions_of(sys.executable) == get_distributions()
