from faker.providers import BaseProvider


class CinemaProvider(BaseProvider):
    formats = (
        '{{city}}',
    )

    def cinema(self, exhibitor=None):
        """
        :param exhibitor: The exhibitor name to use
        :type exhibitor: string
        :example: Royal Kino Sydneyberg
        """
        pattern = self.random_element(self.formats)
        if exhibitor is None:
            pattern = '{{exhibitor}} %s' % pattern
            return self.generator.parse(pattern)
        else:
            return '{0} {1}'.format(exhibitor, self.generator.parse(pattern))
