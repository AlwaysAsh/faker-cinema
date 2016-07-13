import pytest

from faker_cinema import FakerCinema


@pytest.fixture
def faker_with_providers():
    return FakerCinema()
