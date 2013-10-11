'''
 Retrieve the html content from the URL : http://www.chromatic.io/FQrLQsb
'''

import urllib

def wget(url, filename):
    ufile = urllib.urlopen(url)  ## get file-like object for url
    info = ufile.info()   ## meta-info about the url content
    if info.gettype() == 'text/html':
        urllib.urlretrieve(url, filename)
        
def main():
    url = 'http://www.chromatic.io/FQrLQsb'
    print 'Retrieving site content from : %s ' % (url)
    wget(url, '../html/gallery.html')
    print 'Done'
        
if __name__ == '__main__':
  main()            