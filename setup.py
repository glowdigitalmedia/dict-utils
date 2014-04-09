from setuptools import setup, find_packages

setup(
    name='dict-utils',
    version='0.1',
    url='https://www.github.com/andreagrandi/dicts-utils/',
    author='Andrea Grandi',
    author_email='a.grandi@gmail.com',
    description='Simple framework for creating REST APIs',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    test_suite = 'tests.test_dict_utils'
)
