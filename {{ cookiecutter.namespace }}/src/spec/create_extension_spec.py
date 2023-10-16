# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec

# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""{{ cookiecutter.description }}""",
        name="""{{ cookiecutter.namespace }}""",
        version="""{{ cookiecutter.version }}""",
        author=list(map(str.strip, """{{ cookiecutter.author }}""".split(","))),
        contact=list(map(str.strip, """{{ cookiecutter.email }}""".split(","))),
    )

    # TODO: specify either the neurodata types that are used by the extension
    # or the namespaces that contain the neurodata types used. Including the
    # namespace will include all neurodata types in that namespace.
    # This is similar to specifying the Python modules that need to be imported
    # to use your new data types.
    # ns_builder.include_type("ElectricalSeries", namespace="core")
    ns_builder.include_namespace("core")

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information
    tetrode_series = NWBGroupSpec(
        neurodata_type_def="TetrodeSeries",
        neurodata_type_inc="ElectricalSeries",
        doc="An extension of ElectricalSeries to include the tetrode ID for each time series.",
        attributes=[NWBAttributeSpec(name="trode_id", doc="The tetrode ID.", dtype="int32")],
    )

    # TODO: add all of your new data types to this list
    new_data_types = [tetrode_series]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "spec"))
    export_spec(ns_builder, new_data_types, output_dir)
    print("Spec files generated. Please make sure to run `pip install .` to load the changes.")


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
