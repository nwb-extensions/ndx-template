import os
from pynwb import load_namespaces
{{ cookiecutter.py_pkg_name }}_specpath = os.path.join(os.path.dirname(__file__), 'spec', '{{ cookiecutter.namespace }}.namespace.yaml')
load_namespaces({{ cookiecutter.py_pkg_name }}_specpath)
