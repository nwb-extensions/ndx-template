## About

[![Build Status](https://dev.azure.com/nwb-extensions/ndx-template/_apis/build/status/nwb-extensions.ndx-template?branchName=master)](https://dev.azure.com/nwb-extensions/ndx-template/_build/latest?definitionId=1&branchName=master)

This repo provides a template for creating Neurodata Extensions (NDX) for the
[Neurodata Without Borders: Neurophysiology](http://neurodatawithoutborders.github.io/)
 data standard.

We currently support creating Neurodata Extensions only using Python.
MATLAB support is in development.

## Getting started

1. Install [cookiecutter](https://pypi.org/project/cookiecutter/) and [nwb-docutils](https://pypi.org/project/nwb-docutils/).
`cookiecutter` is a Python-based command-line utility that creates projects from templates.
```bash
python -m pip install cookiecutter "nwb-docutils>=0.3.1"
```
2. Run cookiecutter on your local working directory:
```bash
cookiecutter gh:nwb-extensions/ndx-template
```
3. Answer the prompts, which will be used to fill in the blanks throughout the
template automatically. You will be prompted for:
    - `namespace` - The name of the namespace for your NDX. This could be a
    description of the extension (e.g. "ndx-cortical-surface") or the name of your
    lab or group (e.g. "ndx-allen-institute")
      - Namespaces should generally follow the following naming conventions:
        - Use only lower-case ASCII letters (no special characters)
        - Use "-" to separate different parts of the name (no spaces allowed)
        - Use the naming schema "ndx-myname", e.g., "ndx-cortical-surface"
        - Use short and descriptive names
    - `description` - A description of your extension in simple terms
    - `dev_language` - Language for developing your extension (Python, MATLAB,
       Neither)
      - If you want to include custom classes and functionality with your
        extension, please select the language in which those classes are written.
      - If you intend your extension to be loaded without custom classes, select
        Neither.
    - `author` - Your name
    - `email` - Your email address
    - `github_username` - Your username on GitHub
    - `copyright` - Copyright statement, if desired
    - `version` - Version of your extension. Versioning should start at 0.1.0.
    - `release` - Release category, e.g. alpha, beta, official
4. A new directory with the same name as your entered `namespace` will be
created. See `NEXTSTEPS.md` in that directory for the next steps in creating
your awesome new Neurodata Extension.

When you are done creating your extension, we encourage you to follow the steps
to publish your Neurodata Extension for the benefit of the greater neuroscience
community! :)

## Maintainers
- [@rly](https://github.com/rly)
- [@oruebel](https://github.com/oruebel)
- [@ajtritt](https://github.com/ajtritt)
- [@bendichter](https://github.com/bendichter)
