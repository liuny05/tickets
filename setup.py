from setuptools import setup

setup(
    name='tickets',
    version = '0.2',
    description = 'Get tickets info via 12306',
    author = 'aweight',
    py_modules=['tickets', 'stations'],
    install_requires=['urllib3', 'docopt', 'prettytable', 'colorama'],
    entry_points={
        'console_scripts': ['tickets=tickets:cli']
    }
)