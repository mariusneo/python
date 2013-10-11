'''
    Suppose that the resolution of the screen is 1280 * 1024
    create a gallery as an application of the dynamic programming 
    partition problem.
    
    @see http://www.crispymtn.com/stories/the-algorithm-for-a-perfectly-balanced-photo-gallery
    
    For simplicity, algorithm used for balancing the photo gallery, is coded in python
    generating a fixed-with sized gallery.
''' 

import PIL
from PIL import Image

import os
import sys

def list_dir_sorted(path):        
    filenames = os.listdir(path)
    return sorted(filenames, key=lambda s: int(s[3:s.find('.jpg')]))

def partition_array(a, k):
    # get the sum of the elements of the array a
    p = [a[0]]
    for i in range(1, len(a)):
        p.append(p[i-1] + a[i])
        
    # define the array containing min(max(m[i-1, j], p[i] - p[x]), x = range(i)
    # partition table
    m = [[0 for x in range(k)] for x in range(len(a))]
    
    # contains the index of the cut used for retracking the solution
    d = [[0 for x in range(k)] for x in range(len(a))]    
    
    #initialize the first row and column with values
    # so that the dynamic programming algorithm has seed data
    for i in range(len(a)):
        m[i][0] = p[i]
    for i in range(1, k):
        m[0][i] = a[0]
     
    for i in range (1, len(a)):
         for j in range(1, k):
             m[i][j] = sys.maxint
             for x in range(i):
                 #m[i][j], d[i][j] = min(
                 #                       ((max(m[x, [j-1]], p[i] - p[x]), x) for x in range(i))
                 minim = max(m[x][j-1], p[i] - p[x])
                 if m[i][j] > minim:
                     m[i][j] = minim
                     d[i][j] = x 

    # once the partition table has been filled
    # the partitions can be retrieved    
    partitions = []
    low = d[len(a)- 1][k-1]
    high = len(a)
    col = k-1
    while col >= 0 : 
        partitions = [a[low:high]] + partitions
        high = low
        col = col -1
        low = d[low][col]
        
    return partitions

def main():
    filenames = list_dir_sorted('../img/')
    aspect_ratios=[]
    images = {}
    resized_widths=[] 
    sum_widths = 0

    gallery_width =1280    
    gallery_height = 1024
    lines_per_screen = 4
    ideal_height = gallery_height/ lines_per_screen        

    
    for i in range(len(filenames)):
        filename ='../img/'+filenames[i]
        img = Image.open(filename)
        images[filenames[i]] = img
        #aspect_ratio = width / height
        aspect_ratio  = img.size[0]/float(img.size[1])
        aspect_ratios.append(aspect_ratio)
        resized_width = ideal_height *  aspect_ratio
        resized_widths.append(resized_width)
        sum_widths += resized_width
        
    rows = sum_widths/ gallery_width
     
    #Distribute photos over rows using the aspect aspect_ratio as weight
    weights = map(lambda x : x*100, aspect_ratios) 
     
    # now the partition algorithm will be fed with the
    # array of modified widths to be partitioned into
    # rows partition
    partitions = partition_array(weights, int(rows))    
 
        
    
    f = open(os.path.join('../html/', 'newgallery.html'), 'w')
    f.write('<htmL>\n')
    f.write('    <head>\n')
    f.write('        <title>Photo gallery</title>\n')
    f.write('        <style type="text/css">\n');
    f.write('           img{\n');
    f.write('               float:left;\n');
    f.write('              }\n');
    f.write('        </style>');    
    f.write('    </head>\n')
    f.write('    <body>\n')
    f.write('        <div style="width:%spx">\n' % (gallery_width))
    buffer_filenames=[]
    buffer_aspect_ratios = []
    index = 0
    for partition in partitions:
        for unused_i in partition:
            filename ='../img/'+filenames[index]
            buffer_filenames.append(filename)
            buffer_aspect_ratios.append(aspect_ratios[index])
            index += 1

        sum_ratios = reduce(lambda x, y : x+y, buffer_aspect_ratios)            
        for i in range(len(buffer_filenames)):                
           f.write('            <img src="%s" height="%s" width="%s"/>\n' % (buffer_filenames[i], 
                                                                          gallery_width/sum_ratios, 
                                                                          gallery_width/sum_ratios * buffer_aspect_ratios[i]))
        buffer_filenames = []
        buffer_aspect_ratios = []                
    f.write('        </div>')
    f.write('    <body>\n')
    f.write('</html>')    
    f.close()    
    pass


if __name__ == '__main__':
  main()
  
'''
             for x in range(i):
                 m[i][j], d[i][j] = min(
                                        ((max(m[x, [j-1]], p[i] - p[x]), x) for x in range(i))
                 minim = max(m[x][j-1], p[i] - p[x])
                 if m[i][j] > minim:
                     m[i][j] = minim
                     d[i][j] = x 
'''         