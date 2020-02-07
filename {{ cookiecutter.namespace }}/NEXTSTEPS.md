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


## Documenting and Publishing Your Extension to the Community

1. Install the latest release of hdmf_docutils: `python -m pip install hdmf-docutils`

2. Start a git repository for your extension directory {{ cookiecutter.namespace }}
 and push it to GitHub. You will need a GitHub account.
    - Follow these directions:
  https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line

3. Change directory into `docs`.

4. Run `make html` to generate documentation for your extension based on the YAML files.

5. Read `docs/README.md` for instructions on how to customize documentation for
your extension.

6. Modify `README.md` to describe this extension for interested developers.

7. Add a license file. Permissive licenses should be used if possible. **A [BSD license](https://opensource.org/licenses/BSD-3-Clause) is recommended.**

8. Make a release for the extension on GitHub with the version number specified. e.g. if version is {{ cookiecutter.version }}, then this page should exist: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.namespace }}/releases/tag/{{ cookiecutter.version }} . For instructions on how to make a release on GitHub see [here](https://help.github.com/en/github/administering-a-repository/creating-releases).

9. Publish your updated extension on PyPi.
    - Follow these directions: https://packaging.python.org/tutorials/packaging-projects/
    - You may need to modify `setup.py`
    - If your extension version is {{ cookiecutter.version }}, then this page should exist: https://pypi.org/project/{{ cookiecutter.namespace }}/{{ cookiecutter.version }}

   Once your GitHub release and ``setup.py`` are ready, publishing on PyPi:
    ```bash
    python setup.py sdist bdist_wheel
    twine upload dist/*
    ```

10. Go to https://github.com/nwb-extensions/staged-extensions and fork the
repository.

11. Clone the fork onto your local filesystem.

12. Copy the directory `staged-extensions/example` to a new directory
`staged-extensions/{{ cookiecutter.namespace }}`:

    ```bash
    cp -r staged-extensions/example staged-extensions/{{ cookiecutter.namespace }}
    ```

13. Edit `staged-extensions/{{ cookiecutter.namespace }}/ndx-meta.yaml`
with information on where to find your NWB extension.
    - The YAML file MUST contain a dict with the following keys:
      - name: extension namespace name
      - version: extension version
      - src: URL for the main page of the public repository (e.g. on GitHub, BitBucket, GitLab) that contains the sources of the extension
      - pip: URL for the main page of the extension on PyPI
      - license: name of the license of the extension
      - maintainers: list of GitHub
      usernames of those who will reliably maintain the extension
    -

  You may copy and modify the following YAML that was auto-generated:
```yaml
name: {{ cookiecutter.namespace }}
version: {{ cookiecutter.version }}
src: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.namespace }}
pip: https://pypi.org/project/{{ cookiecutter.namespace }}/
license: {{ cookiecutter.license }}
maintainers:
  - {{ cookiecutter.github_username }}
```

14. Edit `staged-extensions/{{ cookiecutter.namespace }}/README.md`
to add information about your extension. You may copy it from
`{{ cookiecutter.namespace }}/README.md`.

  ```bash
cp {{ cookiecutter.namespace }}/README.md staged-extensions/{{ cookiecutter.namespace }}/README.md
```

15. Add and commit your changes to Git and push your changes to GitHub.
```
cd staged-extensions
git add {{ cookiecutter.namespace }}
git commit -m "Add new catalog entry for {{ cookiecutter.namespace }}" .
git push
```

16. Open a pull request. Building of your extension will be tested on Windows,
Mac, and Linux. The technical team will review your extension shortly after
and provide feedback and request changes, if any.

17. When your pull request is merged, a new repository, called
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
