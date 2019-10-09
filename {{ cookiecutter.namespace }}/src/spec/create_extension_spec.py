from pynwb.spec import (
    NWBNamespaceBuilder,
    NWBGroupSpec,
    NWBAttributeSpec,
    NWBDatasetSpec,
    NWBLinkSpec,
    export_spec
)
import os.path


def main():
    # the values for ns_builder are auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(doc='{{ cookiecutter.description }}',
                                     name='{{ cookiecutter.namespace }}',
                                     version='{{ cookiecutter.version }}',
                                     author='{{ cookiecutter.author }}',
                                     contact='{{ cookiecutter.email }}')

    # TODO: define the new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb for more information
    custom_electrical_series = NWBGroupSpec(
        neurodata_type_def='TetrodeSeries',
        neurodata_type_inc='ElectricalSeries',
        doc='An extension of ElectricalSeries to include information about the tetrode ID for each time series.',
        attributes=[
            NWBAttributeSpec(
                name='trode_id',
                doc='The tetrode ID',
                dtype='int'
            )
        ],
    )

    # TODO: add the new data types to this list
    new_data_types = [custom_electrical_series]

    # TODO: include the types that are used by the extension and their namespaces (where to find them)
    ns_builder.include_type('ElectricalSeries', namespace='core')

    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    main()
