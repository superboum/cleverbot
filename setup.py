from setuptools import setup

setup(
    name='Cleverbot',
    version='1.1',
    url='https://github.com/superboum/cleverbot',
    description='A python3 binding of cleverbot wich support special characters.',
    packages=['cleverbot'],
    entry_points={
        'console_scripts': ['cleverbot = cleverbot.cleverbot:main',]
    }
)
