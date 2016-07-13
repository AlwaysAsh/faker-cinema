from faker import Faker

from .exhibitor import ExhibitorProvider
from .cinema import CinemaProvider
from .screen import ScreenProvider
from .cpl import CPLProvider


def FakerCinema():
    fake = Faker()

    fake.add_provider(ExhibitorProvider)
    fake.add_provider(CinemaProvider)
    fake.add_provider(ScreenProvider)
    fake.add_provider(CPLProvider)

    return fake


__author__ = 'Michael Hinstridge'
__all__ = ['ExhibitorProvider', 'CinemaProvider', 'ScreenProvider', 'CPLProvider', 'FakerCinema']
