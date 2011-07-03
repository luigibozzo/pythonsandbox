from mr_directory_scanner import DirectoryScanner
from mr_file_filter import MrFileFilter
from mr_file_name_parser import MrFileNameParser
from mr_google_lucky_catcher import MrGoogleLuckyCatcher
from mr_imdb_page_scraper import MrImdbPageScraper
from mr_movie_info import MrMovieInfo
import sys

if __name__ == "__main__":
    directoryScanner = DirectoryScanner()
    fileFilter = MrFileFilter()
    filenameParser = MrFileNameParser()
    googleLuckyCatcher = MrGoogleLuckyCatcher()
    imdbPageScraper = MrImdbPageScraper()

    if len(sys.argv)<2:
        raise Exception("\n\tUsage: " + sys.argv[0] + " <path_to_scan>")
    folderToScan = sys.argv[1]

    fileFound = directoryScanner.scan_path(folderToScan)

    [matches, skipped] = fileFilter.Filter(fileFound)
    res = list()
    print 'results filter returns %s files' % len(matches)
    for m in matches:
        searchTokens = filenameParser.ParseFileName(m)
        link = googleLuckyCatcher.GetImdbLinkFor(searchTokens)
        [pageContent, rating, title] = imdbPageScraper.Process(link)
        res.append( MrMovieInfo(m, pageContent, rating, link) )

    outFile = open('scan_report.csv', 'w')
    for r in res:
        outFile.writelines(str(r.filename) + '; ' + r.imdbRating + '; ' \
                           + r.imdbPageLink + '; ' + r.imdbPageContent )
    outFile.close()

    outFile = open('scan_report_skipped.csv', 'w')
    for r in skipped:
        outFile.writelines(r.filename)
    outFile.close()
    