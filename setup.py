from distutils.core import setup
from setuptools import setup, find_packages



setup(name='petlodoo',
        version='1.0',
        package_dir={'': '.'},
        #packages=find_packages(),
        packages=['petlodoo', 'petlodoo.io'],
        include_package_data=True,
        )
