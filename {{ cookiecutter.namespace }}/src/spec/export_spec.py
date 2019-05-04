import os

def export_spec(ns_builder, new_data_types):
    '''
    Creates YAML specification files for a new namespace and extensions with
    the given new neurodata types.

    Args:
        ns_builder - pynwb.spec.NWBNamespaceBuilder instance used to build the
                     namespace and extension
        new_data_types - Iterable of NWB Specs that represent new data types
                         to be added
    '''

    if not ns_builder.name:
        raise RuntimeError('Namespace name is required to export specs')

    ns_path = ns_builder.name + '.namespace.yaml'
    ext_path = ns_builder.name + '.extensions.yaml'

    for neurodata_type in new_data_types:
        ns_builder.add_spec(ext_path, neurodata_type)

    ns_builder.export(ns_path, outdir=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', '..', 'spec'))

    print(f'spec/{ns_path} created')
    print(f'spec/{ext_path} created with {len(new_data_types)} data types')
