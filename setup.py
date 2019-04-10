""" Setuptools based iasimage setup module.
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='iasimage',
    version='0.0.2',

    description='iasimage is a utility program for creating IAS images',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/intel/iasimage',

    author='Intel Corporation',
    author_email='huang.jin@intel.com',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='intel ias automotive image',
    py_modules=['iasimage'],

    python_requires='>=2.7',

    install_requires=['cryptography>=2.2.2', 'idna', 'wheel'],

    entry_points={
        'console_scripts': ["iasimage = iasimage:main"],
    },

    test_suite='tests',

    project_urls={
        'Bug Reports': 'https://github.com/intel/iasimage/issues',
        'Source': 'https://github.com/intel/iasimage',
    },
)
