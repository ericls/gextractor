from setuptools import setup, find_packages

setup(
    name="GSpider",
    version="0.1",
    author='ericls',
    author_email='dustet@gmail.com',
    install_requires=[
        "requests",
        "pyquery",
        "six",
    ],
    packages = find_packages()
)
