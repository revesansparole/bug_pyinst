#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {# pkglts, pysetup.kwds
from setuptools import find_packages, setup

setup_kwds = dict(
    name='nitrogen_ferti',
    version="0.1.0",
    description="walou",
    long_description="karoucho",
    author="itk",
    author_email="agro@itk.fr",
    url='https://gitlab.itkweb.fr/nv2/nitrogen_ferti',
    license='private',
    zip_safe=False,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    
    
    package_data={'nitrogen_nferti': []},
    setup_requires=[],
    install_requires=[],
    tests_require=[],
    entry_points={},
    keywords='itk',
    
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
    ],
    )
# #}
# change setup_kwds below before the next pkglts tag


# do not change things below
# {# pkglts, pysetup.call
setup(**setup_kwds)
# #}
