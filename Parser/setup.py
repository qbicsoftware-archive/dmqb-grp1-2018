from setuptools import setup


setup(
    name='Parser',
    version='1.0',
    py_modules=['Parser.py'],
    install_requires=[
        'click',
    ],
    entry_points='''
    [console_scripts]
    hello=hello:cli'''
)
