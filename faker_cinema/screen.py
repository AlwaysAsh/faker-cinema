from faker.providers import BaseProvider


class ScreenProvider(BaseProvider):
    formats = (
        '{{screen_name}} {{screen_number}}',
        '{{screen_name}} {{screen_number}} ({{screen_suffix}})',
    )
    screen_names = (
        'Screen',
        'Theatre',
        'Auditorium',
    )
    screen_suffixes = (
        '3D',
        'IMAX',
        'VIP',
    )

    @classmethod
    def screen_number(cls):
        return cls.numerify(cls.random_element(('%', '%%')))

    @classmethod
    def screen_suffix(cls):
        return cls.random_element(cls.screen_suffixes)

    def screen(self, number=None):
        pattern = self.random_element(self.formats)
        if number is not None:
            pattern = pattern.replace('{{screen_number}}', str(number))
        return self.generator.parse(pattern)

    @classmethod
    def screen_name(cls):
        return cls.random_element(cls.screen_names)