
def getBit(num, index):
    value = num & (1 << index)
    if value == 0:
        return 0
    else:
        return 1
    

print getBit(8,2)
print getBit(8,3)    
print '-' * 50

def setBit(num, index):
    return num | (1 << index)

print setBit(8,0)
print setBit(8,1)
print '-' * 50

def clearBit(num, index):
    mask  = ~ (1 << index)
    return num & mask

print clearBit(15, 2)
print '-' * 50

def updateBit(num, index, v):
    mask  = ~ (1 << index)
    return (num & mask) | (v<<index)

print updateBit(15,2,1)
print updateBit(15,2,0)
print '-' * 50

def clearBitsMSBThroughI(num, index):
    mask = (1 << (index+1)) -1
    return num & mask

print clearBitsMSBThroughI(15, 2)
print clearBitsMSBThroughI(15, 0)
print '-'*50

def clearBitsIThrough0(num, index):
    mask = (1 << (index+1)) -1
    return num & ~mask

print clearBitsIThrough0(15, 2)