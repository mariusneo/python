'''
7.7 Design an algorithm to find the kth number such that the only prime factors are 3,5,7

@author: "neo"

Solution : the factor k of the sequence is the minimum of not yet picked multiples of (3,5,7)
and can be used to produce subsequent factors in the sequence.
'''
from collections import deque
import sys


def getNumber(k):
    # separate the multiples in queues to process them faster
    # element(i) < element(j) in the queue if i<j 
    queue3 = deque([1])
    queue5 = deque([])
    queue7 = deque([])
    
    minValue = 1
    for i in range(k + 1):
        v3 = queue3.popleft()
        v5 = sys.maxint
        if len(queue5) > 0:
            v5 = queue5.popleft()
        v7 = sys.maxint
        if len(queue7) > 0:
            v7 = queue7.popleft()

        minValue = min(v3, v5, v7)
        if v3 == minValue:
            # restore queues that don't contain the minimum
            if v5 != sys.maxint: 
                queue5.appendleft(v5)
            if v7 != sys.maxint:
                queue7.appendleft(v7)
                
            queue3.append(v3 * 3)            
            queue5.append(v3 * 5)
            queue7.append(v3 * 7)
        elif v5 == minValue:
            # restore queues that don't contain the minimum
            if v3 != sys.maxint:
                queue3.appendleft(v3)
            if v7 != sys.maxint:
                queue7.appendleft(v7)

            # avoid having duplicates in the queues queue3 and queue5
            # v5 = 5 * x, but 5*x > 3*x, what means that 3*x was already  
            # processed and at that time 3*5*x was added to queue5, so
            # there is no more need to add 5*3*x to queue3
    
            queue5.append(v5 * 5)
            queue7.append(v5 * 7)
        elif v7 == minValue:
            # restore queues that don't contain the minimum
            if v3 != sys.maxint:
                queue3.appendleft(v3)
            if v5 != sys.maxint: 
                queue5.appendleft(v5)
            
            queue7.append(v7 * 7)
    return minValue        
            

for i in range(20):
    print str(i) + ' - ' + str(getNumber(i))