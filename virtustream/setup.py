#!/usr/bin/python3
"""
Need to automate the install of Fibonacci project into a package to be distributed to the requisite servers. Puppet may be used, although Ansible is a popular tool. A health checks needs to be set up for the webserver to ensure servers are up and sending HTML traffic on port 80.

Test
"""


from setuptools import setup, find_packages

requires = [
    'flask'
]

setup(
    name='fibonacci',
    version='0.0',
    description='Web service to return the nth sequence of Fibonacci numbers',
    author='Felicia Hsieh',
    author_email='214@holbertonschool.com',
    keywords='fibonacci, REST, web service',
    packages='find_packages()',
    include_package_data=True,
    install_requires=requires
)
