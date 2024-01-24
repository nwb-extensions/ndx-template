## About

[![Run tests](https://github.com/nwb-extensions/ndx-template/actions/workflows/run_tests.yml/badge.svg)](https://github.com/nwb-extensions/ndx-template/actions/workflows/run_tests.yml)

This repo provides a template for creating Neurodata Extensions (NDX) for the
[Neurodata Without Borders](https://nwb.org/)
 data standard.

We currently support creating Neurodata Extensions only using Python 3.8+.
MATLAB support is in development.

## Getting started

1. Install [Python](https://www.python.org/downloads/) for your operating system if it is not already installed.

2. Install [cookiecutter](https://pypi.org/project/cookiecutter/) (see [here](https://cookiecutter.readthedocs.io/en/latest/installation.html) for Windows install instructions), [pynwb](https://pypi.org/project/pynwb/), and [hdmf-docutils](https://pypi.org/project/hdmf-docutils/).
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

By default, the project is configured to run code coverage as part of the tests. This is useful to help with creation of tests and report test coverage. However, with this option enabled, breakpoints for debugging with pdb are being ignored. To disable this option for debugging, comment out the following line in your `pyproject.toml`: 

https://github.com/nwb-extensions/ndx-template/blob/3a999dae507a116b4b4775ab3af580112a9e1bb6/%7B%7B%20cookiecutter.namespace%20%7D%7D/pyproject.toml#L82

## Maintainers
- [@rly](https://github.com/rly)
- [@oruebel](https://github.com/oruebel)
- [@jcfr](https://github.com/jcfr)
- [@bendichter](https://github.com/bendichter)
- [@ajtritt](https://github.com/ajtritt)

## Copyright

Neurodata Extensions Catalog (NDX Catalog) Copyright (c) 2021-2024,
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
