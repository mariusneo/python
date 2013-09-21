'''
5.5 Write a function to determine the number of bits required to convert
integer A to integer B.

Example
Input: 31, 14
Output: 2
'''

#print bin(31)
#print bin(14)

def bitdistance(a, b):
    num = a ^ b # first calculate xor to take out the bits which are the same
    
    # calculate the count of 1s
    diff = 0
    while num > 0:
        if num & 1 == 1:
            diff = diff + 1
        num = num >> 1
        
    return diff


print bin(31)
print bin(14)
print 'Distance : ', bitdistance (31, 14)

