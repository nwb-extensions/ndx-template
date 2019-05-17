import os


def export_spec(ns_builder, new_data_types):
    """
    Creates YAML specification files for a new namespace and extensions with
    the given new neurodata types.

    Args:
        ns_builder - pynwb.spec.NWBNamespaceBuilder instance used to build the
                     namespace and extension
        new_data_types - Iterable of NWB Specs that represent new data types
                         to be added
    """

    if 'name' not in ns_builder._NamespaceBuilder__ns_args:
        raise RuntimeError('Namespace name is required to export specs')

    ns_path = ns_builder._NamespaceBuilder__ns_args['name'] + '.namespace.yaml'
    ext_path = ns_builder._NamespaceBuilder__ns_args['name'] + '.extensions.yaml'

    for neurodata_type in new_data_types:
        ns_builder.add_spec(ext_path, neurodata_type)

    ns_builder.export(ns_path, outdir=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', '..', 'spec'))

    print('spec/{ns_path} created'.format(ns_path=ns_path))
    print('spec/{ext_path} created with {new_data_types_count} data types'.format(
        ext_path=ext_path, new_data_types_count=len(new_data_types)))
