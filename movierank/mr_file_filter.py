import os
from stat import ST_SIZE

class MrFileFilter(object):
    def Filter(self, fileFound):
        matches = []
        skipped = []
        for f in fileFound:
            ext = os.path.splitext(f)[1]
            hasAMovieExtentionFilter = ext in ['.mpeg', '.avi']
            hasMinimumSizeFilter = (os.stat(f)[ST_SIZE] / (1024 ** 2)) > 0
#            if hasAMovieExtentionFilter:
            if hasMinimumSizeFilter and hasAMovieExtentionFilter:
                matches.append(f)
            else:
                skipped.append(f)
        print 'Filtered {0} files: {1} matches, {2} skipped'.format(len(fileFound), len(matches), len(skipped))
        return [matches, skipped]
