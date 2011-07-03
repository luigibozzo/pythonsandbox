from tempfile import NamedTemporaryFile
import urllib
from urllib import FancyURLopener
from BeautifulSoup import BeautifulSoup

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

class MrImdbPageScraper(object):
    def Process(self, link):
        myOpener = MyOpener()
        f = myOpener.open(link)
        pageContent = f.read()
        f.close()
        pageContentFile = NamedTemporaryFile(prefix='imdb', delete=False)
        #print 'Dumping page content to file %s ' % pageContentFile.name
        fileHandle = open(pageContentFile.name, 'w')
        fileHandle.write(pageContent)
        fileHandle.close()
        imdbPageContent = pageContentFile.name #'/tmp/imdbkO0lNh'
#        fh = open(imdbPageContent, 'r')
#        pageContent = fh.read()
#        fh.close()
        soup = BeautifulSoup(pageContent)
        ratingNode = soup.find('span', attrs={'class' : 'value', 'itemprop' : 'ratingValue'})
        rating = ratingNode.string
        titleNode = soup.find('title')
        title = titleNode.string
        print 'scraped rank for {0} is [{1}] '.format(title, rating)
        return  [imdbPageContent, rating, title]


