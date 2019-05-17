import os
import shutil
import textwrap


def _select_dev_language():
    dev_language = '{{ cookiecutter.dev_language }}'
    if dev_language != 'Python':
        shutil.rmtree(os.path.join(os.getcwd(), 'src', 'pynwb'))
    if dev_language != 'MATLAB':
        shutil.rmtree(os.path.join(os.getcwd(), 'src', 'matnwb'))


def main():
    """
    Runs the post gen project hook main entry point.
    """
    _select_dev_language()
    print(textwrap.dedent(
        """
        Success! Directory {{ cookiecutter.namespace }} was created with a skeleton for your new NWB:N extension.
        Please see {{ cookiecutter.namespace }}/NEXTSTEPS.md for creating and publishing your extension.
        """
    ))


if __name__ == "__main__":
    main()
