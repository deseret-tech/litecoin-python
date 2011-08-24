from setuptools import setup, find_packages
setup(
    name = "bitcoin-python",
    version = "0.2",
    packages = find_packages("src"),
    package_dir = {'':'src'}
)

