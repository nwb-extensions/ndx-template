## About

This repo provides a template for creating Neurodata Extensions (NDX) for the
[Neurodata Without Borders: Neurophysiology](http://neurodatawithoutborders.github.io/)
 data standard.

We currently support creating Neurodata Extensions only using Python.
MATLAB support is in development.

## Getting started

1. Clone this repository.
2. Install [cookiecutter](https://pypi.org/project/cookiecutter/), a Python-based
command-line utility that creates projects from templates:
```bash
python -m pip install cookiecutter
```
3. Run cookiecutter on your local cloned ndx-template directory:
```bash
cookiecutter ndx-template
```
4. Answer the prompts, which will be used to fill in the blanks throughout the 
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
    - `dev_language` - Language for developing your extension (Python, MATLAB, Neither)
    - `author` - Your name
    - `email` - Your email address
    - `github_name` - Your username on GitHub
    - `copyright` - Copyright statement, if desired
    - `version` - Version of your extension. Versioning should start at 0.1.0.
    - `release` - Release category, e.g. alpha, beta, official
5. A new directory with the same name as your entered `namespace` will be
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
