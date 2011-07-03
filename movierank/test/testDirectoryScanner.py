from unittest import TestCase

from mr_directory_scanner import DirectoryScanner
from test.tempfilescreator import TempFileCreator


class FolderScannerTest(TestCase):
    def setUp(self):
        super(FolderScannerTest, self).setUp()
        self.sut = DirectoryScanner()
        self.tempFilesCreator = TempFileCreator()

    def test_an_empty_folder_scan_returns_an_empty_list(self):
        assert [] == self.sut.scan_path(self.tempFilesCreator.create_empty_folder())

    def test_scanning_a_not_exitent_path_returns_an_empty_list_too(self):
        assert [] == self.sut.scan_path('not_existent_path')

    def test_scanning_a_folder_with_two_files_returns_two_filenames(self):
        folder_with_two_movies = self.tempFilesCreator.create_folder_with_two_movies()
        assert 2 == len(self.sut.scan_path(folder_with_two_movies))
