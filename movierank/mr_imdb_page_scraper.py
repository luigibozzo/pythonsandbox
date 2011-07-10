from tempfile import NamedTemporaryFile
import urllib
from urllib import FancyURLopener
import urllib2
from BeautifulSoup import BeautifulSoup

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

class MrImdbPageScraper(object):
    def Process(self, link):
#        opener = MyOpener()
#        f = opener.open(link)
        proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
        opener = urllib2.build_opener(proxy_support)
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11')]
        f = opener.open(link)
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


