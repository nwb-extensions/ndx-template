"""Test evaluating (baking) the template. Requires pytest-cookies to be installed."""
import os
import sys


def test_bake_project(cookies):
    """Test evaluating the template with default values."""
    sys.path.insert(0, ".")
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "ndx-my-namespace"
    assert result.project_path.is_dir()

    _check_gen_files(result.project_path, "ndx-my-namespace")


def test_bake_project_extra(cookies):
    """Test evaluating the template with namespace set."""
    result = cookies.bake(extra_context={"namespace": "ndx-test"})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "ndx-test"
    assert result.project_path.is_dir()

    _check_gen_files(result.project_path, "ndx-test")


def _check_gen_files(project_dir: str, namespace: str):
    """Test that the correct files are generated after the template is evaluated."""
    for expected_file in [
        # Generated using init_sphinx_extension_doc
        "docs/Makefile",
        "docs/README.md",
        "docs/make.bat",
        "docs/source/_static/theme_overrides.css",
        "docs/source/conf.py",
        "docs/source/conf_doc_autogen.py",
        "docs/source/credits.rst",
        "docs/source/description.rst",
        "docs/source/format.rst",
        "docs/source/index.rst",
        "docs/source/release_notes.rst",
        # Generated using "src/spec/create_extension_spec.py"
        "spec/%s.extensions.yaml" % namespace,
        "spec/%s.namespace.yaml" % namespace,
    ]:
        expected_file = os.path.join(project_dir, expected_file)
        assert os.path.exists(expected_file), f"Missing file: {expected_file}"

        with open(expected_file, "r") as fp:
            assert fp.read().strip() != "", f"Empty file: {expected_file}"


if __name__ == "__main__":
    # python test_bake_project.py ndx-my-namespace ndx-my-namespace
    _check_gen_files(sys.argv[1], sys.argv[2])
