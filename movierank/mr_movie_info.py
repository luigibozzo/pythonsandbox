class MrMovieInfo(object):
    def __init__(self, filename, imdbPageContent, imdbRating, imdbPageLink):
        super(MrMovieInfo, self).__init__()
        self.filename = filename
        self.imdbPageContent = imdbPageContent
        self.imdbRating = imdbRating
        self.imdbPageLink = imdbPageLink