from pynwb.spec import (
    NWBNamespaceBuilder,
    NWBGroupSpec,
    NWBAttributeSpec,
    NWBDatasetSpec,
    NWBLinkSpec
)
from export_spec import export_spec


def main():
    # the values for ns_builder are auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc='{{ cookiecutter.description }}',
        name='{{ cookiecutter.namespace }}',
        version='{{ cookiecutter.version }}',
        author=list(map(str.strip, '{{ cookiecutter.author }}'.split(','))),
        contact=list(map(str.strip, '{{ cookiecutter.email }}'.split(',')))
    )

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

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
