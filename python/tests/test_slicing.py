#! /usr/bin/env python

from numpy.testing import TestCase, run_module_suite
from numpy.testing import assert_equal, assert_almost_equal

from aubio import slice_source_at_stamps
from utils import count_samples_in_file, count_samples_in_directory

import tempfile
import shutil

class aubio_slicing_test_case(TestCase):

    def setUp(self):
        self.source_file = 'chocolate_1min.wav'
        self.output_dir = tempfile.mkdtemp(suffix = 'aubio_slicing_test_case')

    def test_slice_start_only(self):
        regions_start = [i*1000 for i in range(100)]
        slice_source_at_stamps(self.source_file, regions_start, output_dir = self.output_dir)

    def test_slice_start_only_no_zero(self):
        regions_start = [i*1000 for i in range(1, 100)]
        slice_source_at_stamps(self.source_file, regions_start, output_dir = self.output_dir)

    def test_slice_start_beyond_end(self):
        regions_start = [i*1000 for i in range(1, 100)]
        regions_start += [count_samples_in_file(self.source_file)]
        regions_start += [count_samples_in_file(self.source_file) + 1000]
        slice_source_at_stamps(self.source_file, regions_start, output_dir = self.output_dir)

    def tearDown(self):
        original_samples = count_samples_in_file(self.source_file)
        written_samples = count_samples_in_directory(self.output_dir)
        assert_equal(original_samples, written_samples,
            "number samples written different from number of original samples")
        shutil.rmtree(self.output_dir)

if __name__ == '__main__':
    from unittest import main
    main()
