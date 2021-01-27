"""Setup.py for Presidio Image Analyzer and Anonymizer."""
import os.path
from os import path

import setuptools

__version__ = ""
parent_directory = os.path.abspath(
    os.path.join(path.abspath(path.dirname(__file__)), os.pardir)
)
with open(os.path.join(parent_directory, "VERSION")) as version_file:
    __version__ = version_file.read().strip()

setuptools.setup(
    name="presidio_image_anonymizer",
    version=__version__,
    description="Presidio image anonymizer package",
    url="https://github.com/Microsoft/presidio",
    packages=[
        "presidio_image_anonymizer",
    ],
    trusted_host=["pypi.org"],
    tests_require=["pytest", "flake8==3.7.9"],
    install_requires=["flask==1.1.2", "pillow"],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
