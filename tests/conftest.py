from faker import Faker
import pytest

from faker_cinema import ExhibitorProvider, CinemaProvider, ScreenProvider


@pytest.fixture
def faker_with_providers():
    fake = Faker()

    fake.add_provider(ExhibitorProvider)
    fake.add_provider(CinemaProvider)
    fake.add_provider(ScreenProvider)

    return fake
