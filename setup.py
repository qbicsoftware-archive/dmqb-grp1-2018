
from setuptools import setup, find_packages

version = '0.1dev'

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='format validator',
    version=version,
    description='A small validator for formats in the NCBI context',
    long_description=readme,
    keywords=['validator', 'formats', 'bioinformatics'],
    author='Najia Ahmadi and Alexxander Ott',
    license=license,
    scripts=[],  # entry point!! send to parser/cli
    install_requires=required,
    packages=find_packages(exclude='docs'),
    include_package_data=True
)
