#!/usr/bin/env python

from setuptools import setup
from setuptools.command.test import test as TestCommand
import sqlalchemy_sparksql
import sys


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


with open('README.md') as readme:
    long_description = readme.read()

setup(
    name="SparkSQL Driver for SQLAlchemy",
    version=sqlalchemy_sparksql.__version__,
    description="SparkSQL Driver for SQLAlchemy",
    long_description=long_description,
    url='https://github.com/matthsanchez/sqlalchemy-sparksql',
    author="Matt Sanchez",
    author_email="matt at c12.com",
    license="Apache License, Version 2.0",
    packages=['sqlalchemy_sparksql'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Database :: Front-Ends",
    ],
    install_requires=[
        'sqlalchemy>=0.12.0',
        'pyhive[hive]',
    ],
    tests_require=[
        'mock>=1.0.0',
        'pytest',
        'pytest-cov',
        'requests>=1.0.0',
        'sasl>=0.2.1',
        'sqlalchemy>=0.12.0',
        'thrift>=0.10.0',
    ],
    cmdclass={'test': PyTest},
    package_data={
        '': ['*.rst'],
    },
    entry_points={
        'sqlalchemy.dialects': [
            'sparksql = sqlalchemy_sparksql.sparksql:SparkSqlDialect',
        ],
    }
)