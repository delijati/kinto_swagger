""" Setup file.
"""
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()
CHANGES = open(os.path.join(here, "CHANGES.rst")).read()

requires = [
    "kinto",
    "cornice_swagger",
    "pyramid_chameleon",
]

setup(
    name="kinto_swagger",
    version='0.1.0',
    description="Generate swagger from kinto services",
    long_description=README + "\n\n" + CHANGES,
    license="Apache License (2.0)",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords="web services",
    author="Josip Delic",
    author_email="delijati@gmx.net",
    url="https://github.com/delijati/kinto_swaggr",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={
        'test': ["nose", "coverage", ],
    },
    # test_suite='kinto_swagger.tests',
    setup_requires=["setuptools_git"],
)
