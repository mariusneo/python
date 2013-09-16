def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"
    
parrot(1000)
print
parrot(voltage = 1000) #1 keyword argument
print
parrot(voltage = 100000, action = 'VOOOOOM') #2 keyword arguments
print
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
print