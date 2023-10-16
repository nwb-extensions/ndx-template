import os
from pynwb import load_namespaces, get_class

try:
    from importlib.resources import files
except ImportError:
    # TODO: Remove when python 3.9 becomes the new minimum
    from importlib_resources import files

# Get path to the namespace.yaml file with the expected location when installed not in editable mode
__location_of_this_file = files(__name__)
__spec_path = __location_of_this_file / "spec" / "{{ cookiecutter.namespace }}.namespace.yaml"

# If that path does not exist, we are likely running in editable mode. Use the local path instead
if not os.path.exists(__spec_path):
    __spec_path = __location_of_this_file.parent.parent.parent / "spec" / "{{ cookiecutter.namespace }}.namespace.yaml"

# Load the namespace
load_namespaces(str(__spec_path))

# TODO: Define your classes here to make them accessible at the package level.
# Either have PyNWB generate a class from the spec using `get_class` as shown
# below or write a custom class and register it using the class decorator
# `@register_class("TetrodeSeries", "{{ cookiecutter.namespace }}")`
TetrodeSeries = get_class("TetrodeSeries", "{{ cookiecutter.namespace }}")

# If NWBWidgets is installed, create a custom widget for the TetrodeSeries
# neurodata type that displays the trode_id field
# Usage:
#   from nwbwidgets import nwb2widget, default_neurodata_vis_spec
#   vis_spec = default_neurodata_vis_spec
#   vis_spec[TetrodeSeries] = TetrodeSeries.widget
#   nwb2widget(nwbfile, vis_spec)
try:
    from .widgets import TetrodeSeriesWidget

    # add the widget class to the TetrodeSeries class
    TetrodeSeries.widget = TetrodeSeriesWidget

except ImportError:
    # NWBWidgets is not installed, so we cannot create a new widget
    pass

# Remove these functions from the package
del load_namespaces, get_class
