from setuptools import find_packages, setup

setup(
    name="source_organizer",
    version="0.1.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["organize-sources=find_sources:main"]},
)
