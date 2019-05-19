
import os
import sys


def test_post_gen_project_hook(project_dir, namespace):
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
        assert os.path.exists(expected_file)

        with open(expected_file, "r") as fp:
            assert fp.read().strip() != ""


if __name__ == "__main__":
    test_post_gen_project_hook(sys.argv[1], sys.argv[2])
