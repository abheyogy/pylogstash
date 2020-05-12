#!/usr/bin/env python3
'''Program to fetch PortKey monitoring details from Kafka. Process the fetched data in a monitoring
friendly format and further push it back to Kafka.
'''
from setuptools import setup

with open("README", 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='monitoring',
    version='0.0.1',
    description='Transforming Portkey Edge data for Visualising the same.',
    license="SugarBox Private License",
    long_description=LONG_DESCRIPTION,
    author='Pranav Salunke',
    author_email='pranav.salunke@sugarboxnetworks.com',
    url="http://sugarboxnetworks.com/",
    packages=['monitoring'],
    install_requires=['kafka-python'],
)
