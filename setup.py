from setuptools import setup, find_packages

setup(
    name='imhotep_foodcritic',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/scottjab/imhotep_foodcritic',
    license='MIT',
    author='James Scott',
    author_email='scottjab@gmail.com',
    description='An imhotep plugin for chef validation',
    entry_points={
        'imhotep_linters': [
            '.py = imhotep_foodcritic.plugin:FoodCritic'
        ],
    },
)
