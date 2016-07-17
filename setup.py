import json
from os import path

from setuptools import setup, find_packages


def _get_version():
    version_file = path.join(path.abspath(path.dirname(__file__)), 'version.json')

    with open(version_file) as ver:
        version = json.load(ver)
        return '{0}.{1}.{2}'.format(version['major'], version['minor'], version['patch'])


def _get_requirements():
    requirements_txt = path.join(path.abspath(path.dirname(__file__)), 'requirements.txt')

    with open(requirements_txt) as req:
        return [line.strip() for line in req]


setup(
    name='faker_cinema',
    description='A cinema industry-specific provider for faker',
    keywords=['testing', 'faker-provider'],
    version=_get_version(),
    install_requires=_get_requirements(),
    package_dir={'faker_cinema': 'faker_cinema'},
    packages=find_packages(exclude=['*tests*']),
    author='Michael Hinstridge',
    author_email='mhinstridge@gmail.com',
    license='MIT License',
    url='https://github.com/RangerOfFire/faker-cinema',
    download_url='https://github.com/RangerOfFire/faker-cinema/tarball/release/{0}'.format(_get_version()),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License'
    ],
)
