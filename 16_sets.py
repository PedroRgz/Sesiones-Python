#son conjuntos 
#se usa s y t
#son como las listas pero admiten elementos repetidos

s = set([1,2,3])
t = set([3,4,5])

s.union(t) # set([1,2,3,4,5])
s.intersection(t) # set([3])
s.difference(t) # set([1,2])

print(1 in s) #true
print(1 in t) #false
print(1 not in s) #false
print(1 not in t) #true