f = open('..\\in.txt')
output = open('..\\out.txt', 'w')
for line in f:
    output.write(line.rstrip() + '\n')

f.close()
output.close()
