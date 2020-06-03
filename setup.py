from setuptools import find_packages, setup
from package import Package

setup(
    author="Squ1rr3lly",
    author_email="github@squirrelly.anonaddy.com",
    packages=find_packages(),
    include_package_data=True,
    cmdclass={
        "package": Package
    }
)

