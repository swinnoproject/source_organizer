from setuptools import find_packages, setup

setup(
    name="source_organizer",
    version="0.1.0",
    packages=find_packages(),
    entry_points={"console_scritps": ["organize-sources=scripts.find_sources:main"]},
)
