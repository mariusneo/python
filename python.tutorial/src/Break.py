for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print n, 'equals', x, '*', n/x
            break
    else: #else clause belongs to the for loop
        print n, 'is a prime number'