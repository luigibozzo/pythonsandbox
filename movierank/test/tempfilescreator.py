import os
import shutil
from tempfile import mkdtemp, NamedTemporaryFile

class TempFileCreator(object):
    def __init__(self):
        self.listOfFoldersCreated = []

    def create_empty_folder(self):
        f = mkdtemp(prefix='an_empty_folder_for_test')
        self.listOfFoldersCreated.append(f)
        return f

    def __del__(self):
		for f in self.listOfFoldersCreated: shutil.rmtree(f)

    def create_folder_with_two_movies(self):
        d = mkdtemp(prefix='a_movie_folder_for_testing_')
        self.listOfFoldersCreated.append(d)
        NamedTemporaryFile(prefix='a_stub_movie', dir=d, delete=False)
        NamedTemporaryFile(prefix='a_stub_movie2', dir=d, delete=False)
        return d