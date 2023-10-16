from nwbwidgets.ecephys import ElectricalSeriesWidget
from ipywidgets import widgets

from .. import TetrodeSeries


class TetrodeSeriesWidget(ElectricalSeriesWidget):  # this is an HBox
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
