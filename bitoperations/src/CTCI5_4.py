'''
Expain what the following code does : ((n & (n-1)) == 0) 

@author:  neo
'''


for i in range(100):
    if (i & (i-1) == 0):
        print i
        
        
        
'''
By executing the code above can be noticed that the condition
mentioned in the problem returns true only in the case when the
n is a power of 2 (e.g. : 2,4,8,16,32,...)        
'''