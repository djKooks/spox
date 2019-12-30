from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='spox',
    version='0.1.0',
    description='',
    long_description=readme,
    author='',
    author_email='',
    url='',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs'))
)
