import os

class MrFileNameParser(object):
    def ParseFileName(self, fileName):
        print 'parsing tokens from %s ' % fileName
        cleanFilename = os.path.split(fileName)[1]
        cleanFilename = os.path.splitext(cleanFilename)[0]
        cleanFilename = cleanFilename.replace('_', ' ').replace('-', ' ')
        print '-> %s ' % cleanFilename
        return cleanFilename