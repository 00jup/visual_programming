from setuptools import setup, find_packages

setup(
    packages=find_packages(
        where='.',
        include=['homework*'],
        exclude=['homework.tests'],
    ),
)
