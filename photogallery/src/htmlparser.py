'''
  Retrieve the images from the URL : http://www.chromatic.io/FQrLQsb
'''

import re

def extract_image_keys(filename):
    f = open(filename, 'r')
    imagekeys = []
    for line in f:
        #"s3_object_key": "fe766076-f472-e5a5-f173-bded6975ce8a",
        match = re.search(r'^\s+\"s3_object_key":\s+\"(.*)".*$', line)
        if match:
            imagekey = match.group(1)
            imagekeys.append(imagekey)

    return imagekeys

import urllib

def wget(url, filename):
    urllib.urlretrieve(url, filename)

def main():
    imagekeys = extract_image_keys('../html/gallery.html')
    
    # the image key needs to be added to the following URL
    # http://img3.chromatic.io/image_key_comes_here/big.jpg to form an URL like
    # the following:
    # http://img3.chromatic.io/1192ce85-5675-46f0-ddfc-6c49b5ccbb44/big.jpg
    for i in  range(len(imagekeys)):
        imagekey = imagekeys[i]
        url = 'http://img3.chromatic.io/%s/big.jpg' % (imagekey)         
        wget(url, '../img/img%s.jpg'%(i))
    
    

if __name__ == '__main__':
  main()