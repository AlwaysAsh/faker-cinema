Faker Cinema
============

The aim of this package is to provide Cinema Industry specific providers to allow generation of realistic sounding exhibitors,
cinemas and screens.

Pre-requisities
---------------
* You need (Faker)[https://github.com/joke2k/faker]
* Then you will need to add this as a provider to your Faker instance
```
from faker import Faker
from faker_cinema import ExhibitorProvider, CinemaProvider, ScreenProvider


fake = Faker()

fake.add_provider(ExhibitorProvider)
fake.add_provider(CinemaProvider)
fake.add_provider(ScreenProvider)
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

License
-------
Licensed under the MIT License.
