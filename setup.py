from setuptools import setup

setup(
    name='crud',
    version='0.1',
    py_modules=['crud'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        crud=crud:cli
    ''',
)
