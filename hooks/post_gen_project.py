import sys
import textwrap

from hdmf_docutils.init_sphinx_extension_doc import main as init_sphinx_extension_doc
from subprocess import CalledProcessError, check_call


def _generate_doc():
    init_sphinx_extension_doc([
        "--project", """{{ cookiecutter.namespace }}""",
        "--author", """{{ cookiecutter.author }}""",
        "--version", """{{ cookiecutter.version }}""",
        "--release", """{{ cookiecutter.release }}""",
        "--output", "docs",
        "--spec_dir", "spec",
        "--namespace_filename", """{{ cookiecutter.namespace }}.namespace.yaml""",
        "--default_namespace", """{{ cookiecutter.namespace }}""",
        "--custom_description", "description.rst",
        "--custom_release_notes", "release_notes.rst",
    ])


def _create_extension_spec():
    spec_dir = "src/spec"
    sys.path.insert(0, spec_dir)
    check_call([sys.executable, spec_dir + "/create_extension_spec.py"])


def _initialize_git():
    check_call(["git", "init"])
    check_call(["git", "add", "-A"])
    check_call(["git", "commit", "-m", "Initial commit"])
    try:
        # check if the installed version of git created a master branch by default
        # and if so, rename the branch to "main"
        check_call(["git", "show-ref", "--verify", "--quiet", "refs/heads/master"])
        check_call(["git", "branch", "-m", "master", "main"])
    except CalledProcessError:
        pass



def main():
    """
    Runs the post gen project hook main entry point.
    """

    _generate_doc()
    _create_extension_spec()
    _initialize_git()

    print(textwrap.dedent(
        """
        Success! Directory {{ cookiecutter.namespace }} was created with a skeleton for your new NWB extension.
        Please see {{ cookiecutter.namespace }}/NEXTSTEPS.md for creating and publishing your extension.
        """
    ))


if __name__ == "__main__":
    main()
