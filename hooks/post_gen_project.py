from hdmf_docutils.init_sphinx_extension_doc import main as init_sphinx_extension_doc
import shutil
from subprocess import check_call
import sys


def _generate_doc():
    init_sphinx_extension_doc(
        [
            "--project",
            """{{ cookiecutter.namespace }}""",
            "--author",
            """{{ cookiecutter.author }}""",
            "--version",
            """{{ cookiecutter.version }}""",
            "--release",
            """{{ cookiecutter.release }}""",
            "--output",
            "docs",
            "--spec_dir",
            "spec",
            "--namespace_filename",
            """{{ cookiecutter.namespace }}.namespace.yaml""",
            "--default_namespace",
            """{{ cookiecutter.namespace }}""",
            "--custom_description",
            "description.rst",
            "--custom_release_notes",
            "release_notes.rst",
        ]
    )


def _create_extension_spec():
    spec_dir = "src/spec"
    sys.path.insert(0, spec_dir)
    check_call([sys.executable, spec_dir + "/create_extension_spec.py"])


def _initialize_git():
    check_call(["git", "init"])
    check_call(["git", "add", "-A"])
    check_call(["git", "commit", "-m", "Initial commit"])
    check_call(["git", "branch", "-M", "main"])


def _remove_widget_files():
    # The template contains example files for NWB Widgets integration. Many extension creators
    # do not plan to add widgets, so these files add clutter and potential confusion. If the
    # user specifies that they do not want to add widgets, remove these files from the template.
    # This is easier than adding the files only if they want to add widgets.
    dirs_to_remove = {
        "./notebooks",  # currently contains only widget demo -- be more specific if others exist
        "src/pynwb/{{ cookiecutter.py_pkg_name }}/widgets"
    }
    for path in dirs_to_remove:
        print(f"Deleting directory {path}")
        shutil.rmtree(path)


def main():
    """Run the post gen project hook main entry point."""

    if "{{ cookiecutter.widgets }}" == "True":
        _remove_widget_files()

    _generate_doc()
    _create_extension_spec()

    if "{{ cookiecutter.initialize_git }}" == "True":
        _initialize_git()

    print(
        """
Success! Directory {{ cookiecutter.namespace }} was created with a skeleton for your new NWB extension.
Please see {{ cookiecutter.namespace }}/NEXTSTEPS.md for creating and publishing your extension."""
    )


if __name__ == "__main__":
    main()
