from unittest.case import TestCase
from movierank.mr_file_filter import MrFileFilter

class FileFilterTest(TestCase):
    def setUp(self):
        super(FileFilterTest, self).setUp()
        self.sut = MrFileFilter()

    def test_a_newly_created_file_filter_is_not_none(self):
        assert None != self.sut