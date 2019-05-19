
from pynwb.spec import (
    NWBNamespaceBuilder,
    NWBGroupSpec,
    NWBAttributeSpec,
)
from export_spec import export_spec


def main():
    ns_builder = NWBNamespaceBuilder(doc='{{ cookiecutter.description }}',
                                     name='{{ cookiecutter.namespace }}',
                                     version='{{ cookiecutter.version }}',
                                     author='{{ cookiecutter.author }}',
                                     contact='{{ cookiecutter.email }}')

    # TODO: define the new data types
    custom_electrical_series = NWBGroupSpec(
        neurodata_type_def='TetrodeSeries',
        neurodata_type_inc='ElectricalSeries',
        doc='A custom ElectricalSeries for my lab',
        attributes=[
            NWBAttributeSpec(
                name='trode_id',
                doc='the tetrode id',
                dtype='int'
            )
        ],
    )

    # TODO: add the new data types to this list
    new_data_types = [custom_electrical_series]

    # TODO: include the types that are used and their namespaces (where to find them)
    ns_builder.include_type('ElectricalSeries', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
