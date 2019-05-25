# Next Steps for {{ cookiecutter.namespace }} Extension for NWB:N

## Creating Your Extension

1. In a terminal, change directory into the new {{ cookiecutter.namespace }} directory.

2. Add any packages required by your extension to `requirements.txt` and `setup.py`.

3. Run `python -m pip install -r requirements.txt` to install the `pynwb` package
and any other packages required by your extension.

4. Modify `src/create_extension_spec.py` to define your extension.

    - If you want to create any custom classes for interacting with the extension,
      add them to the `src/pynwb`.
      - If present, the `src/pynwb` folder MUST contain the following:
        - `{{ cookiecutter.namespace }}` - Folder with the sources of the NWB extension
        - `{{ cookiecutter.namespace }}/__init__.py` - Python file that may be empty
        - `requirements.txt` - Text file listing the Python package requirements for the extension
        - `README.md` - Markdown file describing the NWB extension
      - If present, the `src/pynwb` folder MAY contain the following files/folders:
        - `test` - Folder for unit tests for the extensions
        - `jupyter-widgets` - Optional package with custom widgets for use with Jupyter

5. Run `python src/spec/create_extension_spec.py` to generate the
`spec/{{ cookiecutter.namespace }}.namespace.yaml` and
`spec/{{ cookiecutter.namespace }}.extensions.yaml` files.

6. You may need to modify `setup.py` and re-run `python setup.py install` if you
use any dependencies.

To ensure the YAML files are distributed with your extension, make sure to
update `setup.py` setting the `package_data` and `include_package_data` keyword parameters:
```python
setup_args = {
    # [...]
    'package_data': {'{{ cookiecutter.py_pkg_name }}': [
        'spec/{{ cookiecutter.namespace }}.namespace.yaml',
        'spec/{{ cookiecutter.namespace }}.extensions.yaml',
    ]},
}
```


## Documenting and Publishing Your Extension to the Community

1. Clone the latest nwb-docutils repository https://github.com/nwb-extensions-test/ndx-template.git
or install the latest release:
`python -m pip install nwb-docutils`
    - If you cloned the latest version, run `python setup.py install` to install nwb-docutils locally.

2. Start a git repository for your extension directory {{ cookiecutter.namespace }}
 and push it to GitHub. You will need a GitHub account.
    - Follow these directions:
  https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line

3. Change directory into `docs`.

4. Run `make html` to generate documentation for your extension based on the YAML files.

5. Read `docs/README.md` for instructions on how to customize documentation for
your extension.

6. Modify `README.md` to describe this extension for interested developers.

7. Add a license file. Permissive licenses should be used if possible.
**BSD license is recommended.**

8. Publish your updated extension on PyPi.
    - Follow these directions: https://packaging.python.org/tutorials/packaging-projects/
    - You may need to modify `setup.py`

9. Go to https://github.com/nwb-extensions/staged-extensions and fork the
repository to your local filesystem.

10. Copy the directory `staged-extensions/example` to a new directory
`staged-extensions/{{ cookiecutter.namespace }}`:

```bash
cp -r staged-extensions/example staged-extensions/{{ cookiecutter.namespace }}
```

11. Edit `staged-extensions/{{ cookiecutter.namespace }}/ndx-meta.yaml`
with information on where to find your NWB extension.
    - The YAML file MUST contain a dict with the following keys:
      - name: {{ cookiecutter.namespace }}
      - version: {{ cookiecutter.version }}
      - src: <URL> : URL to the public repository with the sources of the extension
      - pip: <URL> : URL for installing the extensions from PyPi
      - license: <license> : name of the license of the extension
      - maintainers: {{ cookiecutter.github_name }} : list of GitHub
      usernames of those who will reliably maintain the extension

12. Edit `staged-extensions/{{ cookiecutter.namespace }}/README.md`
to add information about your extension. You may copy it from
`{{ cookiecutter.namespace }}/README.md`.

13. Git commit and push your changes to GitHub.

14. Open a pull request. Building of your extension will be tested on Windows,
Mac, and Linux. The technical team will review your extension shortly after
and provide feedback and request changes, if any.

15. When your pull request is merged, a new repository, called
{{ cookiecutter.namespace }}-feedstock will be created in the nwb-extensions
GitHub organization and you will be added as a maintainer for that repository.


## Updating Your Published Extension

1. Update your {{ cookiecutter.namespace }} GitHub repository.

2. Publish your updated extension on PyPi.

3. Fork the {{ cookiecutter.namespace }}-feedstock repository on GitHub.

4. Open a pull request to test the changes automatically. The technical team
will review your changes shortly after and provide feedback and request changes,
 if any.

5. Your updated extension is approved.
