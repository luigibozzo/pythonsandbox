import os

class DirectoryScanner(object):
    def scan_path(self, aPath):
        res = []
        self.rec_scan_path(aPath, res)
        print 'folder scan found %s files' % len(res)
        return res
    
    def rec_scan_path(self, aPath, res):
        try:
            foundFiles = os.listdir(aPath)
#            print 'scan_path: found {0} files in {1}'.format(len(foundFiles), aPath)
            for f in foundFiles:
                fullPath = os.path.join(aPath, f)
                if os.path.exists(fullPath) == False:
                    print 'WARN: Could not access file {0} '.format(f)
                    continue

#                print 'scan_path: processing %s ' % fullPath
                if os.path.isdir(fullPath):
                    self.rec_scan_path(fullPath, res)
                else:
                    res.append(fullPath)
        except:
            pass
