from faker.providers import BaseProvider


class ExhibitorProvider(BaseProvider):
    formats = (
        '{{exhibitor_name}} {{company_suffix}}',
        '{{exhibitor_shortname}} {{company_suffix}}',
        '{{exhibitor_name}}',
    )
    exhibitor_names = (
        (
            'Fun', 'World', 'Reel', 'Royal', 'View', 'United', 'Super', 'Golden', 'World', 'Star', 'Multi',
            'City', 'Galaxy', 'Palace', 'Magic',
        ),
        (
            'Cinemas', 'Entertainment', 'Kino', 'Theatres', 'Circuit', 'Cine', 'Film',
        ),
    )
    exhibitor_suffixes = (
        'plex', 'polis', 'max', 'mark',
    )
    company_suffixes = (
        'Holdings', 'Corporation', 'Ltd', 'LLC', 'Group',
    )

    @classmethod
    def exhibitor_suffix(cls):
        """
        :example 'plex'
        """
        return cls.random_element(cls.exhibitor_suffixes)

    @classmethod
    def exhibitor_name(cls):
        """
        :example 'World Kino'
        """
        name = []
        for name_part in cls.exhibitor_names:
            name.append(cls.random_element(name_part))

        return ' '.join(name)

    @classmethod
    def exhibitor_shortname(cls):
        """
        :example 'Worldplex'
        """
        return '{0}{1}'.format(cls.random_element(cls.exhibitor_names[0]), cls.random_element(cls.exhibitor_suffixes))

    @classmethod
    def company_suffix(cls):
        """
        :example 'Holdings'
        """
        return cls.random_element(cls.company_suffixes)

    def exhibitor(self):
        """
        :example 'Fun Cinemas LLC'
        """
        pattern = self.random_element(self.formats)
        return self.generator.parse(pattern)
