import urllib
import simplejson

class MrGoogleLuckyCatcher(object):
    def GetImdbLinkFor(self, searchTokens):
        query = 'inurl:imdb ' + searchTokens
        equery = urllib.urlencode({'q' : query})
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s'  % (equery)
        search_results = urllib.urlopen(url)
        json = simplejson.loads(search_results.read())
        results = json['responseData']['results']
        return results[0]['url']
