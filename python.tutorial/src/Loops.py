for i,v in enumerate(['tic', 'tac', 'toe']):
    print i,v
    
    
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print 'What is your {0}? It is {1}.'.format(q, a)
    
    
for i in reversed(range(1,10,2)):
    print i,      
print


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f,
print    
    

#iterate through dictionaries
knights = {'gallahad':'the pure', 'robin':'the brave'}
for k,v in knights.iteritems():
    print k,v
print

words = ['cat', 'window', 'defenestrate']
for w in words[:]: #loop over a slice copy of the entire list, in order to be able to modify the list
    if len(w) > 6:
        words.insert(0,w)
    
print words