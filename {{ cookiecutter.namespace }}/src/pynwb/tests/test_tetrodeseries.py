"""Unit and integration tests for the example TetrodeSeries extension neurodata type.

TODO: Modify these tests to test your extension neurodata type.
"""

import numpy as np

from pynwb import NWBHDF5IO, NWBFile
from pynwb.testing.mock.device import mock_Device
from pynwb.testing.mock.ecephys import mock_ElectrodeGroup, mock_ElectrodeTable
from pynwb.testing.mock.file import mock_NWBFile
from pynwb.testing import TestCase, remove_test_file, NWBH5IOFlexMixin

from {{ cookiecutter.py_pkg_name }} import TetrodeSeries


def set_up_nwbfile(nwbfile: NWBFile = None):
    """Create an NWBFile with a Device, ElectrodeGroup, and 10 electrodes in the ElectrodeTable."""
    nwbfile = nwbfile or mock_NWBFile()
    device = mock_Device(nwbfile=nwbfile)
    electrode_group = mock_ElectrodeGroup(device=device, nwbfile=nwbfile)
    _ = mock_ElectrodeTable(n_rows=10, group=electrode_group, nwbfile=nwbfile)

    return nwbfile


class TestTetrodeSeriesConstructor(TestCase):
    """Simple unit test for creating a TetrodeSeries."""

    def setUp(self):
        """Set up an NWB file. Necessary because TetrodeSeries requires references to electrodes."""
        self.nwbfile = set_up_nwbfile()

    def test_constructor(self):
        """Test that the constructor for TetrodeSeries sets values as expected."""
        all_electrodes = self.nwbfile.create_electrode_table_region(
            region=list(range(0, 10)),
            description="all the electrodes",
        )

        data = np.random.rand(100, 10)
        tetrode_series = TetrodeSeries(
            name="name",
            description="description",
            data=data,
            rate=1000.0,
            electrodes=all_electrodes,
            trode_id=1,
        )

        self.assertEqual(tetrode_series.name, "name")
        self.assertEqual(tetrode_series.description, "description")
        np.testing.assert_array_equal(tetrode_series.data, data)
        self.assertEqual(tetrode_series.rate, 1000.0)
        self.assertEqual(tetrode_series.starting_time, 0)
        self.assertEqual(tetrode_series.electrodes, all_electrodes)
        self.assertEqual(tetrode_series.trode_id, 1)


class TestTetrodeSeriesSimpleRoundtrip(TestCase):
    """Simple roundtrip test for TetrodeSeries."""

    def setUp(self):
        self.nwbfile = set_up_nwbfile()
        self.path = "test.nwb"

    def tearDown(self):
        remove_test_file(self.path)

    def test_roundtrip(self):
        """
        Add a TetrodeSeries to an NWBFile, write it to file, read the file, and test that the TetrodeSeries from the
        file matches the original TetrodeSeries.
        """
        all_electrodes = self.nwbfile.create_electrode_table_region(
            region=list(range(0, 10)),
            description="all the electrodes",
        )

        data = np.random.rand(100, 10)
        tetrode_series = TetrodeSeries(
            name="TetrodeSeries",
            description="description",
            data=data,
            rate=1000.0,
            electrodes=all_electrodes,
            trode_id=1,
        )

        self.nwbfile.add_acquisition(tetrode_series)

        with NWBHDF5IO(self.path, mode="w") as io:
            io.write(self.nwbfile)

        with NWBHDF5IO(self.path, mode="r", load_namespaces=True) as io:
            read_nwbfile = io.read()
            self.assertContainerEqual(tetrode_series, read_nwbfile.acquisition["TetrodeSeries"])


class TestTetrodeSeriesRoundtripPyNWB(NWBH5IOFlexMixin, TestCase):
    """Complex, more complete roundtrip test for TetrodeSeries using pynwb.testing infrastructure."""

    def getContainerType(self):
        return "TetrodeSeries"

    def addContainer(self):
        set_up_nwbfile(self.nwbfile)

        all_electrodes = self.nwbfile.create_electrode_table_region(
            region=list(range(0, 10)),
            description="all the electrodes",
        )

        data = np.random.rand(100, 10)
        tetrode_series = TetrodeSeries(
            name="TetrodeSeries",
            description="description",
            data=data,
            rate=1000.0,
            electrodes=all_electrodes,
            trode_id=1,
        )
        self.nwbfile.add_acquisition(tetrode_series)

    def getContainer(self, nwbfile: NWBFile):
        return nwbfile.acquisition["TetrodeSeries"]
