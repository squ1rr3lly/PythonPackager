from setuptools import find_packages, setup
from package import Package

setup(
    author="UNKNOWN",
    author_email="UNKNOWN",
    packages=find_packages(),
    include_package_data=True,
    cmdclass={
        "package": Package
    }
)

