"""Test evaluating (baking) the template. Requires pytest-cookies to be installed."""
from pathlib import Path
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


def test_bake_project_widgets(cookies):
    """Test evaluating the template with widgets."""
    result = cookies.bake(extra_context={"widgets": True})

    assert result.exit_code == 0
    assert result.exception is None

    for expected_file in [
        "notebooks/example.ipynb",
        "src/pynwb/ndx_my_namespace/widgets/__init__.py",
        "src/pynwb/ndx_my_namespace/widgets/tetrode_series_widget.py",
        "src/pynwb/ndx_my_namespace/widgets/README.md",
    ]:
        expected_file = Path(result.project_path) / expected_file
        assert expected_file.exists(), f"Missing file: {expected_file}"

        with open(expected_file, "r") as fp:
            assert fp.read().strip() != "", f"Empty file: {expected_file}"


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
        expected_file = Path(project_dir) / expected_file
        assert expected_file.exists(), f"Missing file: {expected_file}"

        with open(expected_file, "r") as fp:
            assert fp.read().strip() != "", f"Empty file: {expected_file}"

    # Widgets = False by default, so these files should not exist
    for unexpected_file in [
        "notebooks/example.ipynb",
        "src/pynwb/ndx_my_namespace/widgets/__init__.py",
        "src/pynwb/ndx_my_namespace/widgets/tetrode_series_widget.py",
        "src/pynwb/ndx_my_namespace/widgets/README.md",
    ]:
        unexpected_file = Path(project_dir) / unexpected_file
        assert not unexpected_file.exists(), f"Unexpected file: {unexpected_file}"


if __name__ == "__main__":
    # python test_bake_project.py ndx-my-namespace ndx-my-namespace
    _check_gen_files(sys.argv[1], sys.argv[2])
