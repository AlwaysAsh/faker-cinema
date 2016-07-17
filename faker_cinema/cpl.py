import datetime

from faker.providers import BaseProvider


class CPLProvider(BaseProvider):
    """
    CPL naming convention from http://isdcf.com/dcnc/
    MovieTitle_ContentType{-Modifier}_AspectRatio{-InteriorRatio}_AudioLang-SubLang_Territory-Rating_AudioType_
    Resolution_Studio_Date_Facility_Standard{-3D}_Type
    """
    formats = ('{{content_title}}_{{content_type}}_{{aspect_ratio}}_{{content_language}}_{{cpl_territory}}_'
               '{{audio_type}}_{{cpl_resolution}}_{{cpl_studio}}_{{cpl_date}}_{{cpl_facility}}_{{cpl_standard}}_'
               '{{package_type}}',)

    content_type_modifiers = ('Pre', 'RedBand', 'ALT', '2D', '3D', '48')

    content_type_names = ('FTR', 'TLR', 'TSR', 'PRO', 'RTG', 'POL', 'PSA', 'ADV', 'SHR', 'XSN', 'TST')

    aspect_ratios = ('F', 'S', 'C',)

    content_languages = ('AR', 'BG', 'BS', 'CA', 'CS', 'DA', 'DE', 'EL', 'EN',)

    cpl_territories = ('US', 'UK', 'CA', 'CN', 'FR', 'ES', 'IE', 'IN',)

    audio_types = ('51', '61', '71', '20',)

    audio_type_modifiers = ('HI', 'VI', 'Atmos', 'Auro', 'DTS-X', 'D-box',)

    cpl_resolutions = ('2K', '4K',)

    cpl_studios = ('DI', 'TCF', 'FX', 'LION', 'LFLM', 'MOM', 'MRV', 'PC', 'SPE', 'WR',)

    cpl_date_format = '%Y%m%d'

    cpl_facilities = ('AAM', 'MPS', 'MOL', 'DTU', 'YMA',)

    cpl_standards = ('SMPTE', 'SMPTE-3D',)

    package_types = ('OV', 'VF',)

    def content_title(self):
        pattern = "{{city}}"
        return ''.join(part.title() for part in self.generator.parse(pattern).split(' '))[:14]

    @classmethod
    def content_type_name(cls):
        return cls.random_element(cls.content_type_names)

    @classmethod
    def content_type_modifier(cls):
        return '-'.join(set(cls.random_element(cls.content_type_modifiers) for _ in range(cls.random_int(1, 3))))

    @classmethod
    def aspect_ratio(cls):
        return cls.random_element(cls.aspect_ratios)

    def content_type(self):
        content_type_formats = (
            '{{content_type_name}}',
            '{{content_type_name}}-%',
            '{{content_type_name}}-{{content_type_modifier}}',
            '{{content_type_name}}-%-{{content_type_modifier}}',
        )
        pattern = self.random_element(content_type_formats)

        return self.numerify(self.generator.parse(pattern))

    @classmethod
    def content_language(cls):
        return '-'.join([cls.random_element(cls.content_languages) for _ in range(cls.random_int(1, 2))])

    @classmethod
    def cpl_territory(cls):
        return cls.random_element(cls.cpl_territories)

    @classmethod
    def audio_type(cls):
        audio_type_modifiers = '-'.join(
                set([cls.random_element(cls.audio_type_modifiers) for _ in range(cls.random_int(0, 3))])
        )
        if audio_type_modifiers:
            return '-'.join([
                cls.random_element(cls.audio_types),
                audio_type_modifiers
            ])
        else:
            return cls.random_element(cls.audio_types)

    @classmethod
    def cpl_resolution(cls):
        return cls.random_element(cls.cpl_resolutions)

    @classmethod
    def cpl_studio(cls):
        return cls.random_element(cls.cpl_studios)

    @classmethod
    def cpl_date(cls):
        return datetime.date(
            cls.random_int(min=2009, max=datetime.date.today().year),
            month=cls.random_int(min=1, max=12),
            day=cls.random_int(min=1, max=28),  # Lowest common denominator
        ).strftime(cls.cpl_date_format)

    @classmethod
    def cpl_facility(cls):
        return cls.random_element(cls.cpl_facilities)

    @classmethod
    def cpl_standard(cls):
        return cls.random_element(cls.cpl_standards)

    @classmethod
    def package_type(cls):
        return cls.random_element(cls.package_types)

    def cpl_name(self):
        """
        :example: Thomasbury_TST-8-ALT-48-RedBand_C_CS_IN_20-D-box-VI_4K_LFLM_20110802_AAM_SMPTE-3D_VF
        """
        pattern = self.random_element(self.formats)

        return self.generator.parse(pattern)
