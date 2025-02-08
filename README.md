## About

[![Run tests](https://github.com/nwb-extensions/ndx-template/actions/workflows/run_tests.yml/badge.svg)](https://github.com/nwb-extensions/ndx-template/actions/workflows/run_tests.yml)

This repo provides a template for creating Neurodata Extensions (NDX) for the
[Neurodata Without Borders](https://nwb.org/)
 data standard.

This template currently supports creating Neurodata Extensions only using Python 3.8+.
MATLAB support is in development.

## Getting started

1. Install [Python](https://www.python.org/downloads/) for your operating system if it is not already installed.

2. Install [cookiecutter](https://pypi.org/project/cookiecutter/), [pynwb](https://pypi.org/project/pynwb/), and [hdmf-docutils](https://pypi.org/project/hdmf-docutils/).
`cookiecutter` is a Python-based command-line utility that creates projects from templates.
   ```bash
   python -m pip install -U cookiecutter pynwb hdmf-docutils
   ```
3. Run cookiecutter in the directory where you want to create a new directory with the extension:
   ```bash
   cookiecutter gh:nwb-extensions/ndx-template
   ```

   To overwrite the contents of an existing directory, use the `--overwrite-if-exists` flag:
   ```bash
   cookiecutter --overwrite-if-exists gh:nwb-extensions/ndx-template
   ```
   This can be useful if you want to populate an existing empty git repository with a new extension.
   
4. Answer the prompts, which will be used to fill in the blanks throughout the
template automatically. Guidelines:
    - `Select a name for your extension. It must start with 'ndx-'` - The name of the namespace for your extension. This could be a
    description of the extension (e.g., "ndx-cortical-surface") or the name of your
    lab or group (e.g., "ndx-allen-institute"). The name should generally follow the following naming conventions:
      - Use only lower-case ASCII letters (no special characters)
      - Use "-" to separate different parts of the name (no spaces allowed)
      - Be short and descriptive
    - `Select an initial version string` - Version of your extension. Versioning should start at 0.1.0 and follow [semantic versioning](https://semver.org/) guidelines
    - `Select a license` - Name of license used for your extension source code. A permissive license, such as BSD, should be used if possible.
5. A new folder with the same name as your entered `namespace` will be
created. See `NEXTSTEPS.md` in that folder for the next steps in creating
your awesome new Neurodata Extension.

In case cookiecutter runs into problems and you want to avoid reentering
all the information, you can edit the file `~/.cookiecutter_replay/ndx-template.json`,
and use that via `cookiecutter --replay gh:nwb-extensions/ndx-template`.

See the [PyNWB tutorial](https://pynwb.readthedocs.io/en/stable/tutorials/general/extensions.html) for guidance on how to write your extension.

When you are done creating your extension, we encourage you to follow the steps
to publish your Neurodata Extension in the [NDX Catalog](https://github.com/nwb-extensions/) for the benefit of the
greater neuroscience community! :)

## Running tests with breakpoint debugging

By default, to aid with debugging, the project is configured NOT to run code coverage as part of the tests. Code coverage testing is useful to help with creation of tests and report test coverage. However, with this option enabled, breakpoints for debugging with pdb are being ignored. To enable this option for code coverage reporting, uncomment out the following line in your `pyproject.toml`:

https://github.com/nwb-extensions/ndx-template/blob/11ae225b3fd3934fa3c56e6e7b563081793b3b43/%7B%7B%20cookiecutter.namespace%20%7D%7D/pyproject.toml#L82-L83

## Integrating with NWB Widgets

When answering the cookiecutter prompts, you will be asked whether you would like to create templates for integration with [NWB Widgets](https://github.com/NeurodataWithoutBorders/nwbwidgets), a library of plotting widgets for interactive visualization of NWB neurodata types within a Jupyter notebook. If you answer "yes", then an example widget and example notebook will be created for you. If you answer "no", but would like to add a widget later on, follow the instructions below:

1. Create a directory named `widgets` in `src/pynwb/{your_python_package_name}/`.
2. Copy [`__init__.py`](https://github.com/nwb-extensions/ndx-template/blob/main/%7B%7B%20cookiecutter.namespace%20%7D%7D/src/pynwb/%7B%7B%20cookiecutter.py_pkg_name%20%7D%7D/widgets/__init__.py) to that directory and adapt the contents to your extension.
3. Copy [`tetrode_series_widget.py`](https://github.com/nwb-extensions/ndx-template/blob/main/%7B%7B%20cookiecutter.namespace%20%7D%7D/src/pynwb/%7B%7B%20cookiecutter.py_pkg_name%20%7D%7D/widgets/tetrode_series_widget.py) to that directory and adapt the contents to your extension.
4. Create a directory named `notebooks` in the root of the repository.
5. Copy [example.ipynb](https://github.com/nwb-extensions/ndx-template/blob/main/%7B%7B%20cookiecutter.namespace%20%7D%7D/notebooks/example.ipynb) to that directory and adapt the contents to your extension.
6. Add `nwbwidgets` to `requirements-dev.txt`.

## Maintainers
- [@rly](https://github.com/rly)
- [@oruebel](https://github.com/oruebel)
- [@jcfr](https://github.com/jcfr)
- [@bendichter](https://github.com/bendichter)
- [@ajtritt](https://github.com/ajtritt)

## Copyright

Neurodata Extensions Catalog (NDX Catalog) Copyright (c) 2021-2025,
The Regents of the University of California, through Lawrence
Berkeley National Laboratory (subject to receipt of any required
approvals from the U.S. Dept. of Energy).  All rights reserved.

If you have questions about your rights to use or distribute this software,
please contact Berkeley Lab's Intellectual Property Office at
IPO@lbl.gov.

NOTICE.  This Software was developed under funding from the U.S. Department
of Energy and the U.S. Government consequently retains certain rights.  As
such, the U.S. Government has been granted for itself and others acting on
its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the
Software to reproduce, distribute copies to the public, prepare derivative
works, and perform publicly and display publicly, and to permit others to do so.
