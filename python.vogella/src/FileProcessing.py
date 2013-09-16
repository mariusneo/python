f = open("..\\in.txt")
print f
for line in f:
    print line.rstrip()
f.close()    