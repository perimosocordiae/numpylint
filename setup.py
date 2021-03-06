#!/usr/bin/env python
from setuptools import setup

version = "0.0.1"
setup(
    name='numpylint',
    version=version,
    description='Linter for numeric python code',
    author='CJ Carey',
    author_email='perimosocordiae@gmail.com',
    url='http://github.com/perimosocordiae/numpylint',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    packages=['numpylint'],
    install_requires=['rope'],
    scripts=[
        'numpylint/numpylinter.py',
    ]
)
