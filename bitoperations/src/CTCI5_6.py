'''

5.6 Write a program to swap odd and even bits in an integer with as few instructions
as possible (e.g. bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

@author: neo
'''


def swapBits(a):
    evenBitsShifted =  (a & 0b10101010) >> 1
    oddBitsShifted =   (a & 0b01010101) << 1
    
    print bin(evenBitsShifted)
    print bin(oddBitsShifted)
    
    aSwapped = evenBitsShifted | oddBitsShifted
    return aSwapped


a = 31
print bin(a)
print bin(swapBits(a))