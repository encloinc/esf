from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='esf',

    version='1.0.0',

    description='ESF, the easy way to write and save files in an array format',
    long_description=long_description,

    url='https://github.com/encloinc/esf/',

    author='EncloCreations',
    author_email='jelch2002@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3',
    ],

    keywords=['files', 'saving', 'arrays'],

    py_modules=['esf'],

    install_requires=['peppercorn'],

)
