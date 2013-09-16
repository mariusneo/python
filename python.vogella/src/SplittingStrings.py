s1 = 'This,is,the,first,string,to,deal,with,however,is,just,a,string,list'
s2 = 'This,is,another,piece,of,the,pie,whatever,pie,it,is'

list1 = s1.split(',')
list2 = s2.split(',')

print(len(list1))
print(len(list2))

difference = list(set(list1).difference(set(list2)))
print(difference)