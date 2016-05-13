from os import path

from setuptools import find_packages, setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='accounts',
    version='1.0',
    description='A personal accounting framework written in python.',
    long_description=long_description,
    url='https://github.com/allonhadaya/accounts',
    author='Allon Hadaya',
    author_email='self@allon.nyc',
    license='MIT',
    packages=find_packages(),
    package_data={
        'accounts': ['../README.md'],
    },
    entry_points={
        'console_scripts': [
            'accounts=accounts.main:main',
        ],
    },
)
