import re
from os.path import join, dirname

from setuptools import setup, find_packages


# reading package version (without reloading it)
with open(join(dirname(__file__), 'cliargpars', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S) \
        .match(v_file.read()) \
        .group(1)


setup(
    name='cliargpars',
    version=package_version,
    description='A cli argpars',
    author='Mohammad Sheikhian',
    author_email='mohammadsheikhian70@gmail.com',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    entry_points={
        'console_scripts': [
            'cliargpars=cliargpars.cli:main'
        ]
    },
)

