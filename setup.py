from setuptools import setup

with open('requirements.txt') as f:
    requirements = [ i.strip() for i in f.read().splitlines() ]

exec(open('ranpy_sdk/version.py').read())

setup(
    name="ranpy_sdk",
    version=__version__,
    description='SDK to access Book database',
    author="ranpy-sdk",
    maintainer="Venu",
    packages=["ranpy_sdk"],
    install_requires=requirements,
    include_package_data=True
)
