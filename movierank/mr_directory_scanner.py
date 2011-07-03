import os

class DirectoryScanner(object):
    def scan_path(self, aPath):
        res = []
        self.rec_scan_path(aPath, res)
        print 'folder scan found %s files' % len(res)
        return res
    
    def rec_scan_path(self, aPath, res):
        print 'scan_path: looking into %s ' % aPath
        try:
            foundFiles = os.listdir(aPath)
            print 'scan_path: found %s' % foundFiles
            for f in foundFiles:
                fullPath = os.path.join(aPath, f)
                print 'scan_path: processing %s ' % fullPath
                if os.path.isdir(fullPath):
                    self.rec_scan_path(fullPath, res)
                else:
                    res.append(fullPath)
        except:
            pass
