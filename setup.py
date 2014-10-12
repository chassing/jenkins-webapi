#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup


classifiers = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
    'Operating System :: POSIX :: Linux',
]

kw = {
    'name':             'jenkins-webapi',
    'version':          '0.3.0',
    'description':      'Module for interacting with the Jenkins CI server',
    'long_description': open('README.rst').read(),
    'author':           'Georgi Valkov',
    'author_email':     'georgi.t.valkov@gmail.com',
    'license':          'Revised BSD License',
    'url':              'https://github.com/gvalkov/jenkins-webapi',
    'keywords':         'jenkins ci',
    'classifiers':      classifiers,
    'py_modules':       ['jenkins'],
    'install_requires': ['requests>=2.4.3'],
    'tests_require':    open('requirements-dev.txt').readlines(),
    'zip_safe':         True,
}

if __name__ == '__main__':
    setup(**kw)
