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
    keywords='faker-provider',
    version=_get_version(),
    install_requires=_get_requirements(),
    package_dir={'faker_cinema': 'faker_cinema'},
    packages=find_packages(exclude=['*tests*']),
    author='Michael Hinstridge',
    author_email='mhinstridge@gmail.com',
    license='MIT License',
)
