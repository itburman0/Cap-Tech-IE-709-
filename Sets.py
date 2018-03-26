#Sets are lists with no duplicate entries.
print(set("my name is Isiah and Isiah is my name".split()))

#find out who attendend both meetings persay

a = set(["Jake", "Isiah", "Eric"])
b = set(["Isiah", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

#Find out who attended only one of the events, use the "symmetric_difference" method:
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))


#Difference method
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))
print(b.difference(a))


#Union, combine all people
a = set(["Jake", "John", "Isiah"])
b = set(["John", "Jill"])

print(a.union(b))

#Ending Exercise
#Who attended A but not B

a = ["Jake", "John", "Isiah"]
b = ["John", "Jill"]

A = set(a)
B = set(b)

print(A.difference(B))