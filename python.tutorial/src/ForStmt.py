# Measure some strings
words = ['cat', 'window', 'defensive']

for w in words:
    print w, len(w)


for w in words[:]: #Loop over a slice copy of the entire list
    words.insert(0, w)
    
print words