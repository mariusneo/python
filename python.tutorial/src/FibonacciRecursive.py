def fib(n): # write Fibonacci series up to n
    """ Write Fibonacci series up to n"""
    a,b = 0,1
    while a<n:
        print a,
        a,b = b, a+b
    
    
# now call the previously defined function
fib(200)
print
    
myfunction = fib
myfunction(20)
print
print


def fib2(n): # Return the Fibonacci series up to n
    """ Return a list containing the Fibonacci series up to n"""
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b, a+b
    
    return result
    
    
l = fib2(50)
print l
