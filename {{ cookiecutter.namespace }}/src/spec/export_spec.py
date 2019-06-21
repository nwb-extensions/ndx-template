import os
import warnings

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

    if len(new_data_types) == 0:
        warnings.warn('No data types specified. Exiting.')
        return

    if ns_builder.name is None:
        raise RuntimeError('Namespace name is required to export specs')

    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    output_dir = os.path.join(project_dir, 'spec')

    ns_path = ns_builder.name + '.namespace.yaml'
    ext_path = ns_builder.name + '.extensions.yaml'

    if len(new_data_types) > 1:
        pluralize = 's'
    else:
        pluralize = ''

    print('Creating file {output_dir}/{ext_path} with {new_data_types_count} data type{pluralize}'.format(
        pluralize=pluralize, output_dir=output_dir, ext_path=ext_path,
        new_data_types_count=len(new_data_types)))

    for neurodata_type in new_data_types:
        ns_builder.add_spec(ext_path, neurodata_type)

    print('Creating file {output_dir}/{ns_path}'.format(output_dir=output_dir, ns_path=ns_path))

    ns_builder.export(ns_path, outdir=output_dir)
