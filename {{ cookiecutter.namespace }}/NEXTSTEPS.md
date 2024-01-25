{% set github_username_list = cookiecutter.github_username.split(', ') %}

# Next Steps for {{ cookiecutter.namespace }} Extension for NWB

## Creating Your Extension

1. In a terminal, change directory into the new {{ cookiecutter.namespace }} directory: `cd {{ cookiecutter.namespace }}`

2. Add any packages required by your extension to the `dependencies` key in `pyproject.toml`.

3. Run `python -m pip install -e .` to install your new extension Python package
and any other packages required to develop, document, and run your extension.

4. Modify `src/spec/create_extension_spec.py` to define your extension.

5. Run `python src/spec/create_extension_spec.py` to generate the
`spec/{{ cookiecutter.namespace }}.namespace.yaml` and
`spec/{{ cookiecutter.namespace }}.extensions.yaml` files.

6. Define API classes for your new extension data types.

    - As a starting point, `src/pynwb/__init__.py` includes an example for how to use
      the `pynwb.get_class` to generate a basic Python class for your new extension data
      type. This class contains a constructor and properties for the new data type.
    - Instead of using `pynwb.get_class`, you can define your own custom class for the
      new type, which will allow you to customize the class methods, customize the
      object mapping, and create convenience functions. See the
      [Extending NWB tutorial](https://pynwb.readthedocs.io/en/stable/tutorials/general/extensions.html)
      for more details.

7. Define tests for your new extension data types in `src/pynwb/tests` or `src/matnwb/tests`.
A test for the example `TetrodeSeries` data type is provided as a reference and should be
replaced or removed.

     - Python tests should be runnable by executing [`pytest`](https://docs.pytest.org/en/latest/)
     from the root of the extension directory. Use of PyNWB testing infrastructure from
     `pynwb.testing` is encouraged (see
     [documentation](https://pynwb.readthedocs.io/en/stable/pynwb.testing.html)).
     - Creating both **unit tests** (e.g., testing initialization of new data type classes and
     new functions) and **integration tests** (e.g., write the new data types to file, read
     the file, and confirm the read data types are equal to the written data types) is
     highly encouraged.
     - By default, the project is configured NOT to run code coverage as part of the tests.
     Code coverage reporting is useful to help with creation of tests and report test coverage.
     However, with this option enabled, breakpoints for debugging with pdb are being ignored.
     To enable this option for code coverage reporting, uncomment out the following line in
     your `pyproject.toml`: [line](https://github.com/nwb-extensions/ndx-template/blob/11ae225b3fd3934fa3c56e6e7b563081793b3b43/%7B%7B%20cookiecutter.namespace%20%7D%7D/pyproject.toml#L82-L83
)

8. You may need to modify `pyproject.toml` and re-run `python -m pip install -e .` if you
use any dependencies.

9. Update the `CHANGELOG.md` regularly to document changes to your extension.


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

8. Update the `CHANGELOG.md` to document changes to your extension.

8. Push your repository to GitHub. A default set of GitHub Actions workflows is set up to
test your code on Linux, Windows, Mac OS, and Linux using conda; upload code coverage
stats to codecov.io; check for spelling errors; check for style errors; and check for broken
links in the documentation. For the code coverage workflow to work, you will need to
set up the repo on codecov.io and uncomment the "Upload coverage to Codecov" step
in `.github/workflows/run_coverage.yml`.

8. Make a release for the extension on GitHub with the version number specified. e.g. if version is {{ cookiecutter.version }}, then this page should exist: https://github.com/{{ github_username_list[0] }}/{{ cookiecutter.namespace }}/releases/tag/{{ cookiecutter.version }} . For instructions on how to make a release on GitHub see [here](https://help.github.com/en/github/administering-a-repository/creating-releases).

9. Publish your updated extension on [PyPI](https://pypi.org/).
    - Follow these directions: https://packaging.python.org/en/latest/tutorials/packaging-projects/
    - You may need to modify `pyproject.toml`
    - If your extension version is {{ cookiecutter.version }}, then this page should exist: https://pypi.org/project/{{ cookiecutter.namespace }}/{{ cookiecutter.version }}

   Once your GitHub release and `pyproject.toml` are ready, publishing on PyPI:
    ```bash
    python -m pip install --upgrade build twine
    python -m build
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
      - maintainers: list of GitHub usernames of those who will reliably maintain the extension
    - You may copy and modify the following YAML that was auto-generated:

      ```yaml
      name: {{ cookiecutter.namespace }}
      version: {{ cookiecutter.version }}
      src: https://github.com/{{ github_username_list[0] }}/{{ cookiecutter.namespace }}
      pip: https://pypi.org/project/{{ cookiecutter.namespace }}/
      license: {{ cookiecutter.license }}
      maintainers: {% for username in github_username_list %}
        - {{ username }}
      {%- endfor %}
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
{{ cookiecutter.namespace }}-record will be created in the nwb-extensions
GitHub organization and you will be added as a maintainer for that repository.


## Updating Your Published Extension

1. Update your {{ cookiecutter.namespace }} GitHub repository.

2. Publish your updated extension on PyPI.

3. Fork the {{ cookiecutter.namespace }}-record repository on GitHub.

4. Open a pull request to test the changes automatically. The technical team
will review your changes shortly after and provide feedback and request changes,
if any.

5. Your updated extension is approved.
