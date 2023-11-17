
from setuptools import setup, find_packages

setup(
    name='test',
    packages=find_packages(
        where='.',
        include=['mypackage.*'],
        exclude=['mypackage.tests'],
    ),

)
