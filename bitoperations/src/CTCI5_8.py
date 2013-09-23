'''
5.8 A monochrome screen is stored as a single array of bytes, allowing eight
consecutive pixels to be stored in one byte. The screen has width w, where w is
dividable by 8 (that is, no byte will be split across rows). The height of the 
screen, of course, can be derived from the length of the array and the width.
Implement a function

drawHorizontalLine(screen, width, x1, x2, y) which draws a horizontal line from
(x1, y) to (x2, y).

@author neo
'''


def drawHorizontalLine(screen, width, x1, x2, y):
    x1Offset = x1%8
    x1FullByte = x1/8
    
    if x1Offset != 0:
        x1FullByte = x1FullByte + 1
    
    x2Offset = x2%8
    x2FullByte = x2/8
    if x2Offset != 7:
        x2FullByte = x2FullByte - 1
    
    # fill the full bytes between x1 and x2 with the 0xAA mask
    for i in range(x1FullByte, x2FullByte):
        screen[width*y + i] = 0xFF

    x1ByteMask = 0xFF >> x1Offset
    x2ByteMask = ~(0xFF >> x2Offset) & 0xFF
    
    
    # fill the start and end byte
    if x1FullByte == x2FullByte:
        mask = x1 & x2
        screen[width*y + x1/8] =  screen[width*y + x1/8] | mask
    else:
        pass
        screen[width*y + x1/8] =  screen[width*y + x1/8] | x1ByteMask
        screen[width*y + x2/8] =  screen[width*y + x2/8] | x2ByteMask
    
    
    


# build up the byte array
arr = []
for i in range(100):
    arr.append(0)
    
screen = bytearray(arr)

#for b in screen:
#    print bin(b),

width = 10

x1 = 2*8 + 2
x2 = 6*8 + 3

y = 5

drawHorizontalLine(screen, width, x1, x2, y)
for i in range(len(screen)):
    if i%10 == 0:
        print
    print bin(screen[i]).rjust(10),

  