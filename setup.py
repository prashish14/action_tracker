#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from pip.req import parse_requirements
import io
import os
import sys

pkgname = 'action_tracker'
version = '0.0.0'


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tracker', '-vrsx']
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

install_reqs = parse_requirements('requeriments.txt')
install_requires = [str(i.req) for i in install_reqs]

def readme():
    try:
        os.system('pandoc --from=markdown --to=rst README.md -o README.rst')
        with open('README.rst') as f:
            return f.read()
    except:
        return 'Automantic compress files after upload'


setup(name=pkgname,
      url='https://github.com/nokiadev/action_tracker',
      download_url='https://github.com/nokiadev/action_tracker/tarball/v%s/' % version,
      author="Nokia",
      author_email='valdergallo@gmail.com',
      keywords=['django', 'manager', 'tracker',],
      description='Action Tracker',
      long_description=readme(),
      license='GPL(v3)',
      classifiers=[
          'Framework :: Django',
          'Operating System :: OS Independent',
          'Topic :: Action Tracker',
          'Topic :: Project Manager',
          'Topic :: Internet',
          'Topic :: Other/Nonlisted Topic',
          'Topic :: Software Development',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
      ],
      include_package_data=True,
      version=version,
      install_requires=install_requires,
      # tests_require: tests_require,
      cmdclass={'test': PyTest},
      packages=find_packages(where='.',
                             exclude=('*test*', '*example*', 'runtest')),
)
