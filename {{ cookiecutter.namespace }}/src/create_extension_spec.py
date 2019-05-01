from pynwb.spec import NWBDatasetSpec, NWBNamespaceBuilder, NWBGroupSpec, NWBLinkSpec
import os

doc = '{{ cookiecutter.description }}'

# define the new data types
new_data_types = []
new_data_types.append(NWBGroupSpec(
    default_name='compartments',
    neurodata_type_def='Compartments',
    neurodata_type_inc='DynamicTable',
    doc='table that holds information about what places are being recorded',
    datasets=[
        NWBDatasetSpec(name='number',
                       neurodata_type_inc='VectorData',
                       doc='cell compartment ids corresponding to a each column in the data',
                       dtype='int'),
        NWBDatasetSpec(name='number_index',
                       neurodata_type_inc='VectorIndex',
                       doc='maps cell to compartments',
                       quantity='?'),
        NWBDatasetSpec(name='position',
                       neurodata_type_inc='VectorData',
                       doc='position of recording within a compartment. 0 is close to soma, 1 is other end',
                       dtype='float',
                       quantity='?'),
        NWBDatasetSpec(name='position_index',
                       neurodata_type_inc='VectorIndex',
                       doc='indexes position',
                       quantity='?'),
        NWBDatasetSpec(name='label',
                       neurodata_type_inc='VectorData',
                       doc='labels for compartments',
                       dtype='text',
                       quantity='?'),
        NWBDatasetSpec(name='label_index',
                       neurodata_type_inc='VectorIndex',
                       doc='indexes label',
                       quantity='?')
    ]
))
new_data_types.append(NWBGroupSpec(
    neurodata_type_def='CompartmentSeries',
    neurodata_type_inc='TimeSeries',
    doc='Stores continuous data from cell compartments',
    links=[
        NWBLinkSpec(name='compartments',
                    target_type='Compartments',
                    doc='meta-data about compartments in this CompartmentSeries',
                    quantity='?')
    ]
))

ns_name = '{{ cookiecutter.namespace }}'
ns_builder = NWBNamespaceBuilder(doc=doc,
                                 name=ns_name,
                                 version='{{ cookiecutter.version }}',
                                 author='{{ cookiecutter.author }}',
                                 contact='{{ cookiecutter.email }}')

# must include types that are used and their namespaces (where to find them)
ns_builder.include_type('VectorData', namespace='core')
ns_builder.include_type('VectorIndex', namespace='core')
ns_builder.include_type('TimeSeries', namespace='core')
ns_builder.include_type('DynamicTable', namespace='core')

# Export
ns_path = ns_name + '.namespace.yaml'
ext_path = ns_name + '.extensions.yaml'

for neurodata_type in new_data_types:
    ns_builder.add_spec(ext_path, neurodata_type)
ns_builder.export(ns_path, outdir=os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'spec'))

print(f'spec/{ns_path} created')
print(f'spec/{ext_path} created')