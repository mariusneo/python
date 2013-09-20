'''
  Display all the permutations of a given array.
  
  e.g. : permutations([1,2,3]) --> [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
'''

class Permutations:
    def valid(self, st, k):
        for i in range(k):
            if st[i] == st[k]:
                return False
        return True
    
    def iterativePermutations(self, arr):
        n = len(arr)
        st = [-1]*n
        k = 0
        while k >= 0:
            valid = False
            while not(valid) and st[k]<n :
                st[k] = st[k]+1
                valid = self.valid(st, k)
            if (st[k] < n):
                if (k == n-1):
                    for i in range(len(st)):
                        print arr[st[i]],
                    print
                else:
                    k = k+1
                    st[k] = -1
            else:
                k = k-1
                
    def recursivePermutations(self, arr, st, k):
        if k == len(arr):
            for i in range(len(st)):
                print arr[st[i]],
            print
        else:
            for i in range(len(arr)):
                st[k] = i
                if self.valid(st,k):
                    self.recursivePermutations(arr, st, k+1)
                                        

p = Permutations()
p.iterativePermutations([1,2,3])
print
p.recursivePermutations([1,2,3], [0,0,0], 0)
print



def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                #nb str[0:1] works in both string and list contexts
                yield perm[:i] + str[0:1] + perm[i:]
                
for perm in all_perms('abc'):
    print perm

                