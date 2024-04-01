# If NWBWidgets is installed, create a custom widget for the TetrodeSeries
# neurodata type.
#
# You will also need to update the `vis_spec` dictionary in `__init__.py` so
# that nwbwidgets can find your custom visualizations.
#
# Example usage:
#   from nwbwidgets import nwb2widget, load_extension_widgets_into_spec
#   load_extension_widgets_into_spec([{{ cookiecutter.py_pkg_name }}])
#   nwb2widget(nwbfile)

try:
    from nwbwidgets.ecephys import ElectricalSeriesWidget
    from ipywidgets import widgets

    from .. import TetrodeSeries

    # TODO define your own custom widget for your extension neurodata type
    # using TetrodeSeriesWidget as an example.
    class TetrodeSeriesWidget(ElectricalSeriesWidget):  # this is an HBox
        """Show the trode_id above the ElectricalSeries widget"""

        def __init__(self, tetrode_series: TetrodeSeries, **kwargs):
            super().__init__(electrical_series=tetrode_series, **kwargs)
            vbox = widgets.VBox(
                children=[
                    self._create_trode_id_box(tetrode_series),
                    widgets.HBox(children=list(self.children)),
                ]
            )
            self.children = [vbox]

        def _create_trode_id_box(self, tetrode_series: TetrodeSeries):
            field_lay = widgets.Layout(
                max_height="40px",
                max_width="600px",
                min_height="30px",
                min_width="130px",
            )
            key = widgets.Label("trode_id:", layout=field_lay)
            val = widgets.Label(str(tetrode_series.trode_id), layout=field_lay)
            return widgets.HBox(children=[key, val])

    # add the widget class to the TetrodeSeries class
    TetrodeSeries.widget = TetrodeSeriesWidget

except ImportError:
    print("NWBWidgets is not installed, so we cannot create a new widget.")  # noqa: T201
    print("Run `pip install nwbwidgets` to install NWBWidgets.")  # noqa: T201
