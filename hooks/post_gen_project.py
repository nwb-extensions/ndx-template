import os
import shutil

dev_language = '{{ cookiecutter.dev_language }}'
if dev_language != 'Python':
    shutil.rmtree(os.path.join(os.getcwd(), 'src', 'pynwb'))
if dev_language != 'MATLAB':
    shutil.rmtree(os.path.join(os.getcwd(), 'src', 'matnwb'))

print('\nSuccess! Directory {{ cookiecutter.namespace }} was created with a skeleton for your new NWB:N extension.\n'
      f'Please see {{ cookiecutter.namespace }}/NEXTSTEPS.md for creating and publishing your extension.')
