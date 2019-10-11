import os
from pynwb import load_namespaces
{{ cookiecutter.namespace }}_specpath = os.path.join(os.path.dirname(__file__),
                                                     'spec',
                                                     '{{ cookiecutter.namespace }}.namespace.yaml')
load_namespaces({{ cookiecutter.namespace }}_specpath)
