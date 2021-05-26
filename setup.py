#!/usr/bin/env python

"""The setup script."""
from re import search
from setuptools import setup, find_packages

with open("faraday_agent_parameters_types/__init__.py", "rt", encoding="utf8") as f:
    version = search(r"__version__ = \"(.*?)\"", f.read()).group(1)


with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as history_file:
    history = history_file.read()

requirements = [
    "marshmallow>=3.11.0",
]

setup_requirements = [
    "pytest-runner",
]

extra_req = {
    "dev": ["giteasychangelog", "flake8", "pre-commit", "black"],
    "test": [
        "pytest",
        "pytest-cov",
    ],
    "docs": [
        "mkdocs",
        "mkdocs-material",
    ],
}

setup(
    author="Faraday Development Team",
    author_email="devel@infobytesec.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="""The faraday agents run code remotely to ensure your domains. This info is triggered and published
    to a faraday server instance, which had set the parameters of the code. This repository sets the models to be used
    by both sides.""",
    install_requires=requirements,
    extras_require=extra_req,
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="faraday",
    name="faraday_agent_parameters_types",
    packages=find_packages(),
    setup_requires=setup_requirements,
    url="https://github.com/infobyte/faraday_agent_parameters_types",
    version=version,
    zip_safe=False,
)
