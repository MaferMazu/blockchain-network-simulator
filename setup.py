#!/usr/bin/env python
"""Package metadata for simulator."""
import os

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as f:
    README = f.read()


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.

    Returns:
        list: Requirements file relative path strings
    """
    requirements = set()
    for path in requirements_paths:
        with open(path, 'r', encoding='utf-8') as requirements_file:
            requirements.update(
                line.split('#')[0].strip() for line in requirements_file.readlines()
                if is_requirement(line.strip())
            )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement.

    Returns:
        bool: True if the line is not blank, a comment, a URL, or
              an included file
    """
    return line and not line.startswith(('-r', '#', '-e', 'git+', '-c'))


setup(
    name='blockchain-network-simulator',
    version=1.0,
    description="""This is a blockchain network simulator in Python.""",
    long_description=README,
    author='Maria Fernanda Magallanes, Alfredo Cruz',
    author_email='mafer.mazu8@gmail.com, alfrejcruz@gmail.com',
    packages=[
        'commands',
    ],
    include_package_data=True,
    install_requires=load_requirements('requirements/base.txt'),
    python_requires=">=3.8",
    zip_safe=False,
    keywords='Blockchain Network Simulator',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': [
            'genIdenti = commands.cli:gen_identi',
            'genTransac = commands.cli:gen_transac',
            'nodo = commands.cli:node',
            'exploradorBloque = commands.cli:explorer_block',
            'exploradorTransac = commands.cli:explorer_transac',
        ],
    },
)
