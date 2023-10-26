# This module is imported by nwbwidgets when
# nwbwidgets.load_extension_widgets_into_spec([{{ cookiecutter.py_pkg_name }}])
# is called. Otherwise, the module is not imported unless explicitly imported.

from .tetrode_series_widget import TetrodeSeriesWidget
from .. import TetrodeSeries

vis_spec = {
    TetrodeSeries: TetrodeSeriesWidget,
}
