
from setuptools import setup, find_packages

setup(
    name='exam_1_package',
    version='0.1',
    packages=find_packages(
        where='.',
        include=['exam_1_package.*'],
        exclude=['exam_1_package.tests'],
    ),

)
