from setuptools import setup, find_packages

setup(
    name='dict-utils',
    version='0.1.2',
    url='https://github.com/glowdigitalmedia/dict-utils/',
    author='Andrea Grandi',
    author_email='a.grandi@gmail.com',
    description='Set of utilities and accessory methods to work with Python dicts.',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    test_suite = 'tests.test_dict_utils'
)
