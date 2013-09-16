word = 'Path' + 'A'
print(word)

print('<' + word*5 + '>')

#content of the strings can't be changed in Python.  
anotherword = 'x' + word[1:]
print(anotherword)

print(word[:2] + word[2:])

print (word[1:100])

print(word[-2]) #prints 'h'

s = 'supercalifragilisticexpialidocious'
print(len(s))

unicodestring = u'Hello\u0020World !'
print(unicodestring)