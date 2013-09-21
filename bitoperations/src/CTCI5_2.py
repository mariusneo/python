'''
From 'Cracking the coding interview' book
5.2 Given a real number between 0 and 1 (e.g. : 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately
in binary with less that 32 characters, print "ERROR".
'''

def binaryStr(num):
    if num >=1 or num <=0:
        return "ERROR"
    
    binary = "."
    
    while num > 0:
        if len(binary) > 32:
            return "ERROR"
        
        rest = num * 2
        if rest >= 1:
            binary = binary + "1"
            num = rest -1
        else:
            binary = binary + "0"
            num = rest

    return binary
            

print binaryStr(0.5)
print binaryStr(0.75)
print binaryStr(0.625)            