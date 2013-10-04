'''
7.4 Write methos to implement the multiply, substract, and divide operations for integers.
Use only the add operator.
'''
from decimal import DivisionByZero

def multiply(a, b):
    if a < b:
        return multiply(b, a)
    
    if (a > 0  and b < 0):
        a, b = b, a 
    else:
        if a < 0:
            a = absolute(a)
        if b < 0 :
            b = absolute(b)    
        
    c1 = 0
    s = 0
    while c1 < b:
        c2, t = 1, a
        while c1 + c2 + c2 < b:
            c2, t = c2 + c2, t + t
        s = s + t
        c1 = c1 + c2
    
    return s

def subtract(a, b):
    return a + negate(b)


def divide(a, b):
    if b == 0:
        raise DivisionByZero('integer division by zero')

    negative = False
    if a< 0:
        a = absolute(a)
        if b < 0:
            b = absolute(b)
        else:
            negative = True
    else:
        if b < 0:
            b = absolute(b)
            negative = True
    
    c1 = 0
    s = 0
    while c1 < a:
        c2, t = b, 1
        while c1 + c2 + c2 < a:
            c2, t = c2 + c2, t + t
        c1, s = c1 + c2, s + t
    
    if negative:
        return negate(s)
    else:    
        return s
    

def negate(a):
    if a < 0:
        return absolute(a)
    c1 = 0
    s = 0
    while c1 < a:
        c2, t = 1, -1
        while c1 + c2 + c2 < a:
            c2, t = c2 + c2, t + t
        c1 = c1 + c2
        s = s + t
    
    return s 


def absolute(a):
    if a >= 0 :
        return a
    c1 = 0
    s = 0
    while c1 > a:
        c2, t = -1, 1
        while c1 + c2 + c2 > a:
            c2, t = c2 + c2, t + t
        c1 = c1 + c2
        s = s + t
    
    return s    

print '---------------- MULTIPLY -------------' 
print multiply(8, 15)
print multiply(8, -15)
print multiply(-8, 9)
print multiply(-8, -9)
print '---------------- SUBSTRACT -------------'
print subtract(10, 2)
print subtract(10, -2)
print subtract(-10, -2)
print subtract(-10, 2)
print '---------------- DIVIDE -------------'
print divide(8, 2)
print divide(10, 2)
print divide(10, -2)
print divide(0, -2)
print divide(-10, -2)
