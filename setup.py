from setuptools import setup, find_packages
import sys, os

# Don't import gym module here, since deps may not be installed
for package in find_packages():
    if '_gym_' in package:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), package))
from package_info import USERNAME, VERSION

setup(name='{}-{}'.format(USERNAME, 'gym-gridworld'),
    version=VERSION,
    description='OpenAI Gym custom environment - Sutton & Barto classic Grid World',
    url='https://github.com/miquelramirez/gym-gridworld',
    author='Miquel Ramirez',
    author_email='miquel.ramirez@gmail.com',
    license='MIT License',
    packages=[package for package in find_packages() if package.startswith(USERNAME)],
    package_data={ '{}_{}'.format(USERNAME, 'gym_gridworld'): ['assets/*.cfg' ] },
    zip_safe=False,
    install_requires=[ 'gym>=0.8.0' ],
)
