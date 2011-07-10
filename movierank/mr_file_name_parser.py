from datetime import datetime
import os
import re


class MrFileNameCleaner(object):
    def Clean(self, fileName):
        cleanFilename = os.path.split(fileName)[1]
        cleanFilename = os.path.splitext(cleanFilename)[0]
        cleanFilename = cleanFilename + ' '
        cleanFilename = cleanFilename.upper().replace('_', ' ')\
                                            .replace('-', ' ')\
                                            .replace('DVDRIP', ' ')\
                                            .replace('DVD RIP', ' ')\
                                            .replace('XVID', ' ')\
                                            .replace('DIVX', ' ')\
                                            .replace('DVDSCR', ' ')\
                                            .replace('DVD SCR', ' ')\
                                            .replace('AC3', ' ')\
                                            .replace('CD1', ' ')\
                                            .replace('CD 1', ' ')\
                                            .replace('CD2', ' ')\
                                            .replace('CD 2', ' ')\
                                            .replace('SUBBED', ' ')\
                                            .replace('SILENT', ' ')\
                                            .replace('ITALIAN', ' ')\
                                            .replace('SATRIP', ' ')

        cleanFilename = self.RemoveURLs(cleanFilename)
        cleanFilename = self.RemoveParenthesisedText(cleanFilename)
        cleanFilename = cleanFilename.replace('.', ' ')

        print '{0}\t\t{1} '.format(cleanFilename, fileName)
        return cleanFilename

    def RemoveURLs(self, fileName):
        topLevelDomains = ".COM .IT .ORG".split()
        for tld in topLevelDomains:
            tldWithBlank = tld + ' '
            tldIdx = fileName.find(tldWithBlank)
            if  tldIdx != -1:
                blankIdx = fileName.rfind(' ', 0, tldIdx)
                if  blankIdx != -1:
                    rightIdx = (tldIdx + len(tld))
                    stringToBeRemoved = fileName[blankIdx:rightIdx]
                    left = fileName[0:blankIdx]
                    right = fileName[rightIdx:len(fileName)]
                    print 'URL Removing: {0} from {1}'.format(stringToBeRemoved, fileName)
                    return left+right
        return fileName

    def RemoveParenthesisedText(self, fileName):
        patternsToSearchFor = ['\(.*\)', '\[.*\]']
        for p in patternsToSearchFor:
            m = re.search(p, fileName)
            if m != None:
#                print 'Find parenthesised text! {0} -> will be skipped'.format(m.group(0))
                currMatch = m.group()
                fileName = fileName.replace(currMatch, ' ')
                yearMatch = re.search('[0-9]{4}', currMatch)
                if yearMatch != None:
                    year = int(yearMatch.group(0))
                    now = datetime.now()
                    if year > 1920 and year < (now.year+1):
#                        print 'Found year: {0} (will not be skipped)'.format(year)
                        fileName = fileName + ' ' + str(year)

        return fileName



