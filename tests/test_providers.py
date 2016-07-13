import re

import six

"""
These are more just sanity checks that the functions are called because I'm not actually going to seed Faker and check
the output, sorry!
"""


def test_exhibitor_provider_returns_an_exhibitor_name_string(faker_with_providers):
    result = faker_with_providers.exhibitor()

    assert isinstance(result, six.string_types)


def test_cinema_provider_returns_a_cinema_name_string(faker_with_providers):
    result = faker_with_providers.cinema()

    assert isinstance(result, six.string_types)


def test_cinema_provider_returns_provided_exhibitor_in_cinema_name_when_exhibitor_is_specified(faker_with_providers):
    exhibitor_name = 'Fakehibitor'
    result = faker_with_providers.cinema(exhibitor=exhibitor_name)

    assert exhibitor_name in result


def test_screen_provider_returns_a_screen_name_string(faker_with_providers):
    result = faker_with_providers.screen()

    assert isinstance(result, six.string_types)


def test_screen_provider_returns_the_screen_number_specified(faker_with_providers):
    screen_number = 47  # That's numberwang
    result = faker_with_providers.screen(number=screen_number)

    # Because assert str(screen_number) in result is too easy
    assert screen_number == int(re.split('([0-9]+)', result)[1])


def test_cpl_provider_returns_a_cpl_name_string(faker_with_providers):
    result = faker_with_providers.cpl_name()

    assert isinstance(result, six.string_types)
