# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup_args = {
    'name': '{{ cookiecutter.namespace }}',
    'version': '{{ cookiecutter.version }}',
    'description': '{{ cookiecutter.description }}',
    'author': '{{ cookiecutter.author }}',
    'author_email': '{{ cookiecutter.email }}',
    'url': '',
    'license': '',
    'install_requires': [
        'pynwb'
    ],
    'packages': find_packages(),
    'classifiers': [
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    'zip_safe': False
}

if __name__ == '__main__':
    setup(**setup_args)
