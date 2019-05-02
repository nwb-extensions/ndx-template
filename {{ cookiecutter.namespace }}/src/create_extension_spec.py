from pynwb.spec import NWBNamespaceBuilder
import os

ns_name = '{{ cookiecutter.namespace }}'
ns_builder = NWBNamespaceBuilder(doc='{{ cookiecutter.description }}',
                                 name=ns_name,
                                 version='{{ cookiecutter.version }}',
                                 author='{{ cookiecutter.author }}',
                                 contact='{{ cookiecutter.email }}')

# CHANGEME
# define the new data types
# comparment_series = NWBGroupSpec(
#     neurodata_type_def='CompartmentSeries',
#     neurodata_type_inc='TimeSeries',
#     doc='Stores continuous data from cell compartments',
#     links=[
#         NWBLinkSpec(name='compartments',
#                     target_type='Compartments',
#                     doc='meta-data about compartments in this CompartmentSeries',
#                     quantity='?')
#     ]
# )

# CHANGEME
# add the new data types to this list
# new_data_types = [compartment_series]
new_data_types = []

# CHANGEME
# Must include types that are used and their namespaces (where to find them)
# ns_builder.include_type('TimeSeries', namespace='core')

# Export
ns_path = ns_name + '.namespace.yaml'
ext_path = ns_name + '.extensions.yaml'

for neurodata_type in new_data_types:
    ns_builder.add_spec(ext_path, neurodata_type)

ns_builder.export(ns_path, outdir=os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'spec'))

print(f'spec/{ns_path} created')
print(f'spec/{ext_path} created with {len(new_data_types)} data types')
