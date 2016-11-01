from setuptools import setup

setup(
    name='tickets',
    version = '1.0',
    description = 'Get tickets info via 12306',
    author = 'aweight',
    url = 'https://github.com/liuny05/tickets_12306/',
    py_modules=['tickets', 'stations'],
    install_requires=['urllib3', 'docopt', 'prettytable', 'colorama'],
    entry_points={
        'console_scripts': ['tickets=tickets:cli']
    }
)