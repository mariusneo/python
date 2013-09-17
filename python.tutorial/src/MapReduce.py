def cube(x): return x*x*x
a = map(cube, range(1,11))
print a

#more than one sequence can be passed
# then the function mus have as many args as sequences
seq = range(8)
def add(x,y): return x+y
sumarr = map(add, seq,seq)
print sumarr


s = reduce(add, range(1,11))
print s
# print reduce(add,[]) would produce an error due to the empty list
# given to the reduce function                   

def sum(seq):
    def add(x,y): return x+y
    return reduce(add, seq, 0)

print(sum(range(1,11)))
print(sum([]))
