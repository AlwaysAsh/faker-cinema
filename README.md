[![Build Status](https://travis-ci.org/RangerOfFire/faker-cinema.svg?branch=master)](https://travis-ci.org/RangerOfFire/faker-cinema)
[![Coverage Status](https://coveralls.io/repos/github/RangerOfFire/faker-cinema/badge.svg?branch=master)](https://coveralls.io/github/RangerOfFire/faker-cinema?branch=master)
Faker Cinema
============

The aim of this package is to provide Cinema Industry specific providers to allow generation of realistic sounding exhibitors,
cinemas and screens.

Pre-requisites
---------------
* You need [Faker](https://github.com/joke2k/faker)
* Then you will need to add this as a provider to your Faker instance (from [the faker documentation](https://github.com/joke2k/faker#how-to-create-a-provider))
```
from faker import Faker
from faker_cinema import ExhibitorProvider, CinemaProvider, ScreenProvider, CPLProvider


fake = Faker()

fake.add_provider(ExhibitorProvider)
fake.add_provider(CinemaProvider)
fake.add_provider(ScreenProvider)
fake.add_provider(CPLProvider)
```

__OR__

* _[New in 0.2.0]_ Just import the FakerCinema factory function:
```
from faker_cinema import FakerCinema

fake = FakerCinema()
```

Usage
-----
Fake cinema chain name (AKA exhibitor name):
```
>>> fake.exhibitor()
'World Theatres Ltd'
```

Fake cinema name:
```
>>> fake.cinema()
'Golden Kino Michaelton'
```

Fake cinema name for a given cinema chain name:
```
>>> exhibitor = fake.exhibitor()
>>> [fake.cinema(exhibitor) for _ in range(3)]
['Super Cine Holdings Shannonport', 'Super Cine Holdings Karamouth', 'Super Cine Holdings South Rhondaberg']
```

Fake screen name:
```
>>> [fake.screen(number) for number in range(1, 4)]
['Screen 1', 'Screen 2 (IMAX)', 'Theatre 3 (3D)']
```

Fake CPL name:
```
>>> fake.cpl_name()
'Hodgechester_PRO-Pre-ALT_C_CA-CS_CA_VI-71-D-box-HI_2K_MRV_20150228_DTU_SMPTE-3D_VF'
```

Development & Testing
---------------------
* Install the requirements and dev requirements:
```
pip install -r requirements.txt -r requirements-dev.txt
```
* Run py.test:
```
py.test
```

Changelog
---------
* __0.2.0:__ Added CPL provider initial version and added FakerCinema factory function
* __0.1.0:__ Initial version with Exhibitor, Cinema and Screen functionality

License
-------
Licensed under the MIT License.
