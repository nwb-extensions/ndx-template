"""Jinja2 extension to allow the use of the zip() function in templates."""
from jinja2.ext import Extension


class ZipExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.globals.update(zip=zip)