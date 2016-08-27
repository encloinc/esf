from setuptools import setup
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ESF',

    
    version='1.0.0',

    description='The easiest way to store data on arrays',
    long_description=long_description,

    url='https://github.com/encloinc/esf',

    author='EncloCreations',
    author_email='jelch2002@gmail.com',

    license='MIT',


    classifiers=[

        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='files esf arrays',
    packages=['none'],

    install_requires=[],


    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    package_data={
        'esf': ['esf'],
    },

  
    data_files=[('my_data', ['data/data_file'])],

    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
