from setuptools import setup, find_packages

setup(
    name="javaclass",
    version="2.0.0",
    author="Marcus LaFerrera (@mlaferrera)",
    url="https://github.com/PUNCH-Cyber/stoq-plugins-public",
    license="Apache License 2.0",
    description="Decodes and extracts information from Java Class files",
    packages=find_packages(),
    include_package_data=True,
    test_suite='tests',
)
