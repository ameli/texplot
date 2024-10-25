#!/usr/bin/env python

# SPDX-FileCopyrightText: Copyright 2021, Siavash Ameli <sameli@berkeley.edu>
# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileType: SOURCE
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the license found in the LICENSE.txt file in the root
# directory of this source tree.


# =======
# Imports
# =======

import setuptools
import os
from os.path import join
import sys
import errno


# ================
# get requirements
# ================

def get_requirements(directory, subdirectory="", filename='requirements',
                     ignore=False):
    """
    Returns a list containing the package requirements given in a file named
    "requirements.txt" in a subdirectory.

    If `ignore` is `True` and the file was not found, it passes without raising
    error. This is useful when the package is build without
    `docs/requirements.txt` and `tests/requirements.txt`, such as in the docker
    where the folders `docs` and `tests` are not copied to the docker image.
    See `.dockerignore` file.
    """

    requirements_filename = join(directory, subdirectory, filename + ".txt")

    # Check file exists
    if os.path.exists(requirements_filename):
        requirements_file = open(requirements_filename, 'r')
        requirements = [i.strip() for i in requirements_file.readlines()]
    else:
        # Ignore if file was not found.
        if ignore:
            requirements = ''
        else:
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), requirements_filename)

    return requirements


# ====
# main
# ====

def main(argv):

    directory = os.path.dirname(os.path.realpath(__file__))
    package_name = "texplot"

    # Version
    version_dummy = {}
    version_file = join(directory, package_name, '__version__.py')
    exec(open(version_file, 'r').read(), version_dummy)
    version = version_dummy['__version__']
    del version_dummy

    # Author
    author_file = join(directory, 'AUTHORS.txt')
    author = open(author_file, 'r').read().rstrip()

    # Requirements
    requirements = get_requirements(directory)
    test_requirements = get_requirements(directory, subdirectory="tests",
                                         ignore=True)
    docs_requirements = get_requirements(directory, subdirectory="docs",
                                         ignore=True)

    # ReadMe
    readme_file = join(directory, 'README.rst')
    long_description = open(readme_file, 'r').read()

    # Description
    description = 'Enhance your matplotlib plots with publication-quality ' + \
        'style'

    # URLs
    url = 'https://github.com/ameli/texplot'
    download_url = url + '/archive/main.zip'
    documentation_url = url + '/blob/main/README.rst'
    tracker_url = url + '/issues'

    # Inputs to setup
    metadata = dict(
        name=package_name,
        version=version,
        author=author,
        author_email='sameli@berkeley.edu',
        description=description,
        long_description=long_description,
        long_description_content_type='text/x-rst',
        keywords="""matplotlib plotting latex""",
        url=url,
        download_url=download_url,
        project_urls={
            "Documentation": documentation_url,
            "Source": url,
            "Tracker": tracker_url,
        },
        platforms=['Linux', 'OSX', 'Windows'],
        packages=setuptools.find_packages(exclude=[
            'tests.*',
            'tests',
            'examples.*',
            'docs.*',
            'docs']
        ),
        install_requires=requirements,
        python_requires='>=3.9',
        setup_requires=[
            'setuptools',
            'wheel'],
        tests_require=[
            'pytest',
            'pytest-cov'],
        include_package_data=True,
        zip_safe=False,  # False: package can be "cimported" by another package
        extras_require={
            'test': test_requirements,
            'docs': docs_requirements,
        },
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: Implementation :: CPython',
            'License :: OSI Approved :: BSD License',
            'Operating System :: POSIX :: Linux',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: MacOS',
            'Natural Language :: English',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Scientific/Engineering',
        ],
    )

    # Setup
    setuptools.setup(**metadata)


# =============
# script's main
# =============

if __name__ == "__main__":
    main(sys.argv)
