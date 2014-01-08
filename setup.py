from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys


here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md', 'CHANGES.txt')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='PerformanceAnalytics',
    version= 0.1,
    url='http://github.com/zsljulius/performanceanalytics',
    license='Apache Software license',
    author='Shenglan Zhang',
    tests_require=['pytest'],
    install_requires=['numpy', 'Pandas'],
    cmdclass={'test': PyTest},
    author_email={'shenglan@empiritrage.com'},
    description='A python implementation of the PerformanceAnalytics in R',
    long_description = long_description,
    packages = ["PerformanceAnalytics"],
    include_package_data=True,
    platforms ='any',
    test_suite='PerformanceAnalytics.test.test_PerformanceAnalytics',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Developers'
    ],
    extras_require ={
        'testing':['pytest']
    }
)
