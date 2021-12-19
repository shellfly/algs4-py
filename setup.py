"""A Python library for book algs4

See:
https://algs4.cs.princeton.edu/home/
https://github.com/shellfly/algs4-py
"""

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="algs4",
    version="1.0.3",
    description="A Python implementation library for book algs4",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shellfly/algs4-py",
    author="shellfly",
    author_email="shell0fly@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="algs4 algorithm",  # Optional
    packages=["algs4", "algs4.utils"],
)
